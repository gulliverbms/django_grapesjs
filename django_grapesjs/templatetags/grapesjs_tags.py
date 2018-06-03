from django_grapesjs.settings import GRAPESJS_SAVE_CSS, GRAPESJS_DEFAULT_MODELS_DATA
from django import template


register = template.Library()


@register.simple_tag
def get_save_css_value():
    return GRAPESJS_SAVE_CSS


@register.simple_tag
def get_default_models_data():
    return GRAPESJS_DEFAULT_MODELS_DATA


