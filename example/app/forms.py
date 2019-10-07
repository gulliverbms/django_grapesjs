from django_grapesjs.forms.base import BaseGrapesJSForm

from app.models import GrapesJSJSONModel


class GrapesJSBuilderForm(BaseGrapesJSForm):
    class Meta:
        model = GrapesJSJSONModel  # noqa: E741
        exclude = tuple()