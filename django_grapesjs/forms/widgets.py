from django import forms
from django.template.loader import render_to_string

from django_grapesjs.settings import GRAPESJS_TEMPLATE, STATIC_URL
from django_grapesjs.template import template_source

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
                STATIC_URL + 'css/django_grapesjs/grapes.min.css',
                STATIC_URL + 'css/django_grapesjs/grapesjs-preset-newsletter.css',
                STATIC_URL + 'css/django_grapesjs/grapesjs-preset-webpage.min.css',
                STATIC_URL + 'css/django_grapesjs/grapesjs-plugin-filestack.css',
            )
        }
        js = [
            '//feather.aviary.com/imaging/v3/editor.js',
            STATIC_URL + 'js/django_grapesjs/grapes.js',
            STATIC_URL + 'js/django_grapesjs/grapesjs-aviary.min.js',
            STATIC_URL + 'js/django_grapesjs/grapesjs-preset-newsletter.min.js',
            STATIC_URL + 'js/django_grapesjs/grapesjs-preset-webpage.min.js',
            STATIC_URL + 'js/django_grapesjs/grapesjs-lory-slider.min.js',
            STATIC_URL + 'js/django_grapesjs/grapesjs-tabs.min.js',
            STATIC_URL + 'js/django_grapesjs/grapesjs-plugin-filestack.min.js',
        ]

    def get_formated_value_id(self, value_id):
        return value_id.replace('-', '_')

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        context['widget']['attrs']['id'] = self.get_formated_value_id(context['widget']['attrs']['id'])
        context['widget'].update({'get_render_html_value': self.get_render_html_value(self.default_html)})
        context['widget'].update({'html_name_init_conf': self.html_name_init_conf})

        return context

    def get_render_html_value(self, default_html, apply_django_tag=False):
        def _get_render_html_value():
            if not apply_django_tag:
                return template_source.get_template(default_html).template

            return render_to_string(default_html)

        return _get_render_html_value

