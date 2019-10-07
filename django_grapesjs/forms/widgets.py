from django import forms
from django_grapesjs import settings
from django_grapesjs.utils import get_render_html_value
from django_grapesjs.utils.get_source import get_grapejs_assets

__all__ = (
    'GrapesJsWidget',
)


class GrapesJsWidget(forms.Textarea):
    """
    Textarea form widget with support grapesjs.
    This is widget base config grapesjs.
    """

    template_name = settings.GRAPESJS_TEMPLATE

    class Media:
        css = {
            'screen': get_grapejs_assets('css'),

        }
        js = get_grapejs_assets('js'),

    def get_formatted_id_value(self, value_id):
        return value_id.replace('-', '_')

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        context['widget']['attrs']['id'] = self.get_formatted_id_value(
            context['widget']['attrs']['id']
        )
        context['widget'].update({
            'get_render_html_value': get_render_html_value(
                self.default_html, apply_django_tag=self.apply_django_tag
            ),
            'html_name_init_conf': self.html_name_init_conf,
            'template_choices': self.template_choices,
            'apply_django_tag': int(self.apply_django_tag),
        })

        return context

