from django.contrib import admin
from django_grapesjs.admin import GrapesJsAdminMixin

from app.models import GrapesJSModel  # noqa: #E501


@admin.register(GrapesJSModel)
class ExampleAdmin(GrapesJsAdminMixin, admin.ModelAdmin):
    pass

