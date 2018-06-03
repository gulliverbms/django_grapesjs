from django.db import models
from django_grapesjs.settings import GRAPESJS_DEFAULT_HTML
from django_grapesjs.forms.widgets import GrapesJsWidget
from django_grapesjs.forms.fields import GrapesJsField

__all__ = (
    'GrapesJsHtmlField',
)


class GrapesJsHtmlField(models.TextField):
    """
    Model field with support grapesjs.

    """
    def __init__(self, verbose_name=None, name=None, auto_now=False,
                 auto_now_add=False, **kwargs):
        self.default_html = kwargs.pop('default_html', GRAPESJS_DEFAULT_HTML)

        super().__init__(verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        kwargs['form_class'] = GrapesJsField
        kwargs['widget'] = GrapesJsWidget
        setattr(kwargs['widget'], 'default_html', self.default_html)

        return super().formfield(**kwargs)

