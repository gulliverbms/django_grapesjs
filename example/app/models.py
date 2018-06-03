from django.db import models
from django_grapesjs.models import GrapesJsHtmlField


class ExampleModel(models.Model):
    html = GrapesJsHtmlField()

