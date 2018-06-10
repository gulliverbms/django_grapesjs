from django import forms

from django_grapesjs.forms import GrapesJsWidget
from django_grapesjs.settings import BASE, GRAPESJS_DEFAULT_HTML, REDACTOR_CONFIG

__all__ = (
    'GrapesJsField',
)


class GrapesJsField(forms.CharField):
    '''
    Form field with support grapesjs.
    '''

    widget = GrapesJsWidget

    def __init__(self, max_length=None, min_length=None, strip=True, empty_value='',
                 default_html=GRAPESJS_DEFAULT_HTML, html_name_init_conf=REDACTOR_CONFIG[BASE],
                 *args, **kwargs):
        super().__init__(max_length=None, min_length=None, strip=True, empty_value='', *args, **kwargs)

        self.widget.default_html = default_html
        self.widget.html_name_init_conf = html_name_init_conf

