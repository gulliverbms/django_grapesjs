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
    def __init__(self, verbose_name=None, name=None, auto_now=False,
                 auto_now_add=False, default_html=GRAPESJS_DEFAULT_HTML,
                 redactor_config=BASE, **kwargs):
        self.default_html = default_html
        self.html_name_init_conf = REDACTOR_CONFIG[redactor_config]

        super().__init__(verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        kwargs['form_class'] = GrapesJsField
        kwargs['widget'] = GrapesJsWidget
        kwargs['default_html'] = self.default_html
        kwargs['html_name_init_conf'] = self.html_name_init_conf

        return super().formfield(**kwargs)

