from django import forms
from django.template.loader import render_to_string

from django_grapesjs.settings import GRAPESJS_TEMPLATE
from django_grapesjs.template import template_source
from django_grapesjs.utils import apply_string_handling

__all__ = (
    'GrapesJsWidget',
)


class GrapesJsWidget(forms.Textarea):
    '''
    Textarea form widget with support grapesjs.
    This is widget base config grapesjs.

    '''
    template_name = GRAPESJS_TEMPLATE

    class Media:
        css = {
            'all': (
                'css/django_grapesjs/grapes.min.css',
                'css/django_grapesjs/grapesjs-preset-newsletter.css',
                'css/django_grapesjs/grapesjs-preset-webpage.min.css',
                'css/django_grapesjs/grapesjs-plugin-filestack.css',
            )
        }
        js = [
            'js/django_grapesjs/feather-aviary-editor.js',
            'js/django_grapesjs/grapes.js',
            'js/django_grapesjs/grapesjs-aviary.min.js',
            'js/django_grapesjs/grapesjs-preset-newsletter.min.js',
            'js/django_grapesjs/grapesjs-preset-webpage.min.js',
            'js/django_grapesjs/grapesjs-lory-slider.min.js',
            'js/django_grapesjs/grapesjs-tabs.min.js',
            'js/django_grapesjs/grapesjs-plugin-filestack.min.js',
        ]

    def get_formated_value_id(self, value_id):
        return value_id.replace('-', '_')

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        context['widget']['attrs']['id'] = self.get_formated_value_id(context['widget']['attrs']['id'])
        context['widget'].update({
            'get_render_html_value': self.get_render_html_value(),
            'html_name_init_conf': self.html_name_init_conf
        })

        return context

    def get_render_html_value(self):
        def _get_render_html_value():
            if not self.apply_django_tag:
                return apply_string_handling(
                    template_source.get_template(self.default_html).template
                )

            return apply_string_handling(render_to_string(self.default_html))

        return _get_render_html_value

