from django.views.generic import TemplateView, FormView
from django_grapesjs.views.mixins import (
    GrapesJSTemplateViewMixin, GrapesJSTemplateProcessingMixin
)


class GrapesJSTemplateView(GrapesJSTemplateViewMixin, TemplateView):
    title = 'Grapes JS'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = self.title
        return context


class GrapesJSFormView(GrapesJSTemplateProcessingMixin, FormView):
    title = 'Grapes JS'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = self.title
        return context