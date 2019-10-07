from django import template
from django.utils.safestring import mark_safe
from django_grapesjs import settings

register = template.Library()


@register.simple_tag
def get_settings_value(name, safe=False):
    """Get a settings value by its name."""
    if not safe:
        return getattr(settings, name)

    return mark_safe(str(getattr(settings, name)))


@register.filter
def get_grapesjs_asset(plugin_name):
    """
    Get grapesjs assets dict with asset paths.
    :param plugin_name: A grapes js plugin name.
    :return: dict: A plugin
    """
    return {
        **{'core': settings.GRAPESJS_CORE_ASSETS},
        **settings.GRAPESJS_PLUGIN_ASSETS
    }


@register.filter
def get_item(dictionary, key):
    """Get a diction item value by a dict key."""
    return dictionary.get(key)


@register.filter
def contains(dictionary, key):
    """Check if key exists in dictionary."""
    return key in dictionary


@register.filter
def get_property(obj, name):
    """Get an object property value by a property name."""
    return getattr(name, obj)


@register.filter
def exists(name):
    """Check if variable with a primitive value does exist."""
    return int(bool(name))
