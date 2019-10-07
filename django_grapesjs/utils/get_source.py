from django.template.loader import render_to_string

from django_grapesjs import settings
from django_grapesjs.template import template_source
from django_grapesjs.utils import apply_string_handling

__all__ = (
    'get_render_html_value',
    'get_grapejs_assets',
    'build_url'
)


def get_render_html_value(default_html, apply_django_tag=False):
    def _get_render_html_value():
        if not apply_django_tag:
            return apply_string_handling(
                template_source.get_template(default_html).template
            )

        return apply_string_handling(render_to_string(default_html))

    return _get_render_html_value


def get_grapejs_assets(type='all'):
    """Provide grapes.js asset of a different type."""
    assets = {
        **{'core': settings.GRAPESJS_CORE_ASSETS},
        **settings.GRAPESJS_PLUGIN_ASSETS
    }

    if type == 'css' or type == 'js':
        return map(lambda plugin_assets: plugin_assets[type], assets.values())

    return assets


def build_url(base: str, arg: str=None):
    """Build client-side urls for grapes.js library."""
    if not arg:
        return base
    parts = list(
        filter(lambda part: part, base.split('/'))
    )
    parts.append(arg)
    return "/" + "/".join(parts)
