import json
from http import HTTPStatus

from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse

from django_grapesjs import settings, get_grapesjs_form, get_grapesjs_model
from django_grapesjs.utils import build_url


class GrapesJSContextData(object):
    """Common context data which is applied to a html page."""

    def get_context_data(self, **additional_context):
        """Get default context."""
        context = super().get_context_data()
        lookup_field = settings.GRAPESJS_MODEL_LOOKUP_FIELD
        context = {
            **context, **{
                'GRAPESJS_STORAGE_ID_PREFIX': settings.GRAPESJS_STORAGE_ID_PREFIX,
                'GRAPESJS_CONTAINER_ID': settings.GRAPESJS_CONTAINER_ID,
                'GRAPESJS_STORAGE_TYPE': settings.GRAPESJS_STORAGE_TYPE,
                'GRAPESJS_CHECK_LOCAL': settings.GRAPESJS_CHECK_LOCAL,
                'GRAPESJS_STEPS_BEFORE_SAVE': settings.GRAPESJS_STEPS_BEFORE_SAVE,
                'GRAPESJS_URL_STORE': build_url(
                    settings.GRAPESJS_URL_STORE,
                    additional_context.get(lookup_field)
                ),
                'GRAPESJS_URL_LOAD': build_url(
                    settings.GRAPESJS_URL_LOAD,
                    additional_context.get(lookup_field)
                ),
                'GRAPESJS_ALLOWED_ORIGIN_LIST': settings.GRAPESJS_ALLOWED_ORIGIN_LIST
            }
        }
        return context


class GrapesJSTemplateViewMixin(GrapesJSContextData):
    """A bare template view mixin for a template view."""

    template_name = 'django_grapesjs/views/base.html'


class GrapesJSTemplateProcessingMixin(GrapesJSContextData):
    """A form class view mixin for a formview."""

    template_name = 'django_grapesjs/views/full.html'
    form_class = lambda: get_grapesjs_form() # noqa: E731
    model_class = lambda: get_grapesjs_model() # noqa: E731

    def get_context_data(self, **additional_context):
        context = super().get_context_data(**additional_context)
        return context

    def get_or_create_a_template(self, **lookup_data):
        """Check whether a template exists in db or create a new model for it."""
        model_class = self.__class__.get_model_class()
        lookup_field = settings.GRAPESJS_MODEL_LOOKUP_FIELD
        return model_class.objects.get_or_create(
            **{lookup_field: lookup_data.get(lookup_field)}
        )

    def get(self, request, *args, **kwargs):
        if not settings.GRAPESJS_MODEL:
            raise ImproperlyConfigured(
                "Invalid or missing a model path to GRAPESJS_MODEL property"
            )
        elif not settings.GRAPESJS_FORM:
            raise ImproperlyConfigured(
                "Invalid or missing a model path to GRAPESJS_FORM property"
            )
        template_model, created = self.get_or_create_a_template(**kwargs)
        context = self.get_context_data(**{
            settings.GRAPESJS_MODEL_LOOKUP_FIELD: str(template_model.id)
        })
        return self.render_to_response(context)


    @classmethod
    def get_form_class(cls):
        return cls.form_class()

    @classmethod
    def get_model_class(cls):
        return cls.model_class()

    @classmethod
    def saveTemplate(cls, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse(status=HTTPStatus.FORBIDDEN, data=None)

        template_data = json.loads(
            request.body.decode('utf-8')
        )
        form_data = {
            'data': template_data,
            'files': request.FILES,
        }
        form_class = cls.get_form_class()
        model_class = cls.get_model_class()
        lookup_field = settings.GRAPESJS_MODEL_LOOKUP_FIELD
        try:
            template_instance = model_class.objects.get(
                **{lookup_field: kwargs[lookup_field]}
            )
            form_data['instance'] = template_instance
        finally:
            grapesjs_form = form_class(**form_data)

        if grapesjs_form.is_valid():
            status = HTTPStatus.OK
            data = grapesjs_form.save().to_dict()
        else:
            status = HTTPStatus.BAD_REQUEST
            data = grapesjs_form.errors
        return JsonResponse(status=status, data=data)

    @classmethod
    def loadTemplate(cls, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse(status=HTTPStatus.FORBIDDEN, data=None)

        model_class = cls.get_model_class()
        lookup_field = settings.GRAPESJS_MODEL_LOOKUP_FIELD

        if not kwargs.get(lookup_field, None):
            return JsonResponse(status=HTTPStatus.OK, data={})

        try:
            template_instance = model_class.objects.get(
                **{lookup_field: kwargs[lookup_field]}
            )
            data = template_instance.to_dict()
        except model_class.DoesNotExist:
            data = {}
        return JsonResponse(status=HTTPStatus.OK, data=data)