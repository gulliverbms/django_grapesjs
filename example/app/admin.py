from django.contrib import admin
from app.models import ExampleModel


@admin.register(ExampleModel)
class ExampleAdmin(admin.ModelAdmin):
    pass

