from importlib import import_module

from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured

from django_grapesjs import settings

__all__ = [
    'get_grapesjs_form'
]


def get_grapesjs_form():
    """Return the GrapesJS form that is active in this project."""
    try:
        path_chunks = settings.GRAPESJS_FORM.split('.')
        module_path = ".".join(path_chunks[0:2])
        module = import_module(module_path)
        return getattr(module, path_chunks[2], None)
    except ImportError as ie:
        raise ImproperlyConfigured(
            "GRAPESJS_FORM refers to form '%s' that has not been installed" % settings.GRAPESJS_FORM
        )


def get_grapesjs_model():
    """Return the GrapesJS template model that is active in this project."""
    try:
        if not settings.GRAPESJS_MODEL:
            # Indicates that user don't use any model
            return settings.GRAPESJS_MODEL
        return django_apps.get_model(settings.GRAPESJS_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("GRAPESJS_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "GRAPESJS_MODEL refers to model '%s' that has not been installed" % settings.GRAPESJS_MODEL
        )
