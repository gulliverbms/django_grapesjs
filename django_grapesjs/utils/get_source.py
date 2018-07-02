from django.template.loader import render_to_string
from django_grapesjs.template import template_source
from django_grapesjs.utils import apply_string_handling

__all__ = ('get_render_html_value', )


def get_render_html_value(default_html, apply_django_tag=False):
    def _get_render_html_value():
        if not apply_django_tag:
            return apply_string_handling(
                template_source.get_template(default_html).template
            )

        return apply_string_handling(render_to_string(default_html))

    return _get_render_html_value

