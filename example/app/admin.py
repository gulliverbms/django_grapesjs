from django.contrib import admin
from app.models import ExampleModel
from django_grapesjs.admin import GrapesJsAdminMixin


@admin.register(ExampleModel)
class ExampleAdmin(GrapesJsAdminMixin, admin.ModelAdmin):
    pass

