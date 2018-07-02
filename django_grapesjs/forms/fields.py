from django import forms

from django_grapesjs.forms import GrapesJsWidget
from django_grapesjs.settings import BASE, GRAPESJS_DEFAULT_HTML, REDACTOR_CONFIG
from django_grapesjs.utils import apply_string_handling

__all__ = (
    'GrapesJsField',
)


class GrapesJsField(forms.CharField):
    '''
    Form field with support grapesjs.
    '''

    widget = GrapesJsWidget

    def __init__(self, default_html=GRAPESJS_DEFAULT_HTML, html_name_init_conf=REDACTOR_CONFIG[BASE],
                 apply_django_tag=False, validate_tags=False, template_choices=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widget.default_html = default_html
        self.widget.html_name_init_conf = html_name_init_conf
        self.widget.apply_django_tag = apply_django_tag
        self.widget.template_choices = template_choices
        self.validate_tags = validate_tags

    def validate(self, value):
        super().validate(value)
        # TODO: check the field
        # if self.validate_tags:

    def clean(self, value):
        value = apply_string_handling(value, 'apply_tag_save')

        return super().clean(value)

