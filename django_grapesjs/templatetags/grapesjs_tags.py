from django import template
from django.utils.safestring import mark_safe
from django_grapesjs import settings


register = template.Library()


@register.simple_tag
def get_settings_value(name, safe=False):
    if not safe:
        return getattr(settings, name)

    return mark_safe(str(getattr(settings, name)))

