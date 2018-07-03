from django.core.management.base import SystemCheckError
from django.db import models

from django_grapesjs.forms.widgets import GrapesJsWidget
from django_grapesjs.forms.fields import GrapesJsField
from django_grapesjs.settings import BASE, GRAPESJS_DEFAULT_HTML, REDACTOR_CONFIG

__all__ = (
    'GrapesJsHtmlField',
)


class GrapesJsHtmlField(models.TextField):
    """
    Model field with support grapesjs.

    """
    def __init__(self, default_html=GRAPESJS_DEFAULT_HTML, redactor_config=BASE,
                 apply_django_tag=False, validate_tags=False, template_choices=None, **kwargs):
        if kwargs.get('choices'):
            raise ValueError(
                "use 'template_choices' instead of 'choices' in the '%s'" % self.__class__.__name__
            )

        if self.check_template_choices(template_choices):
            default_html = template_choices[0][0]

        self.params_for_formfield = {
            'default_html': default_html,
            'html_name_init_conf': REDACTOR_CONFIG[redactor_config],
            'apply_django_tag': apply_django_tag,
            'validate_tags': validate_tags,
            'template_choices': template_choices,
            'form_class': GrapesJsField,
            'widget': GrapesJsWidget,
        }

        super().__init__(**kwargs)

    def formfield(self, **kwargs):
        return super().formfield(**{**kwargs, **self.params_for_formfield})

    def check_template_choices(self, value):
        if not value:
            return False

        self.choices = value
        error = self._check_choices()

        if error:
            error_info = error[0].msg.replace('choices', 'template_choices')
            raise SystemCheckError('\nERROR:\n%s: %s' % (self.__class__.__name__, error_info, ))

        return True

