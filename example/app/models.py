from django.contrib.postgres.fields import HStoreField
from django.utils.translation import ugettext as _
from django.db import models

from django_grapesjs.models.base import BaseGrapesJSModel
from django_grapesjs.models.fields import GrapesJsHtmlField


class GrapesJSModel(models.Model):
    html = GrapesJsHtmlField()


class GrapesJSJSONModel(BaseGrapesJSModel):
    gjs_assets = HStoreField()
    gjs_css = HStoreField()
    gjs_styles = HStoreField()
    gjs_html = HStoreField()
    gjs_components = HStoreField()

    class Meta:
        verbose_name = _('grapes model')
        verbose_name_plural = _('grapesjs models')