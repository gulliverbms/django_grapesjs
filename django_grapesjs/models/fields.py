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
                 apply_django_tag=False, validate=False, **kwargs):
        self.params_for_formfield = {
            'default_html': default_html,
            'html_name_init_conf': REDACTOR_CONFIG[redactor_config],
            'apply_django_tag': apply_django_tag,
            'validate': validate,
            'form_class': GrapesJsField,
            'widget': GrapesJsWidget,
        }

        super().__init__(**kwargs)

    def formfield(self, **kwargs):
        return super().formfield(**{**kwargs, **self.params_for_formfield})

