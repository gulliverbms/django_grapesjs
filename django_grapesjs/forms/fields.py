from django import forms
from django_grapesjs.forms import GrapesJsWidget

__all__ = (
    'GrapesJsField',
)


class GrapesJsField(forms.CharField):
    '''
    Form field with support grapesjs.
    '''

    widget = GrapesJsWidget

