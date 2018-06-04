from django_grapesjs.settings import GRAPESJS_TEMPLATE
from django.template.loader import render_to_string
from django import forms

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
                'https://unpkg.com/grapesjs/dist/css/grapes.min.css',
                'https://unpkg.com/grapesjs-preset-newsletter/dist/grapesjs-preset-newsletter.css',
            )
        }
        js = [
            'https://unpkg.com/grapesjs',
            'https://unpkg.com/grapesjs-preset-newsletter',
        ]

    def get_formated_value_id(self, value_id):
        return value_id.replace('-', '_')

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        context['widget']['attrs']['id'] = self.get_formated_value_id(context['widget']['attrs']['id'])
        context['widget'].update({'get_render_html_value': self.get_render_html_value(self.default_html)})

        return context

    def get_render_html_value(self, default_html):
        def _get_render_html_value():
            return render_to_string(default_html)

        return _get_render_html_value

