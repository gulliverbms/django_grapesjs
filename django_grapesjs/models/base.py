from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.forms import model_to_dict


class BaseGrapesJSModel(models.Model):
    gjs_assets = HStoreField()
    gjs_css = HStoreField()
    gjs_styles = HStoreField()
    gjs_html = HStoreField()
    gjs_components = HStoreField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def to_dict(self):
        return model_to_dict(self)
