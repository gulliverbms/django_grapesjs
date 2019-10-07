from django import forms
from django.forms import fields
from .fields import GrapesJsField


class GrapesJSAdminFormMixin(forms.ModelForm):
    """GrapesJS base form for admin."""
    html = GrapesJsField()


class BaseGrapesJSForm(forms.ModelForm):
    """GrapesJS base form for client-side."""

    gjs_assets = fields.CharField()
    gjs_css = fields.CharField()
    gjs_styles = fields.CharField()
    gjs_html = fields.CharField()
    gjs_components = fields.CharField()
