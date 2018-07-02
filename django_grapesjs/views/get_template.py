from django.http import HttpResponse
from django.views.generic import TemplateView
from django_grapesjs.utils import get_render_html_value

__all__ = ('GetTemplate', )


class GetTemplate(TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = request.GET['template_name']
        apply_django_tag = int(request.GET['apply_django_tag'])

        return HttpResponse(get_render_html_value(template_name, apply_django_tag=apply_django_tag)())

