from django.conf import settings


# path to the html file of the form field. Enter your value for the override
GRAPESJS_TEMPLATE = getattr(settings, 'GRAPESJS_TEMPLATE', 'django_grapesjs/textarea.html')

# True if you want to save html and css
GRAPESJS_SAVE_CSS = int(getattr(settings, 'GRAPESJS_SAVE_CSS', False))

# use the value of the field from the db - True, or use the global save editor
GRAPESJS_DEFAULT_MODELS_DATA = int(getattr(settings, 'GRAPESJS_DEFAULT_MODELS_DATA', True))

# redefine the path to the html file, the markup from this file will be used by default
GRAPESJS_DEFAULT_HTML = getattr(settings, 'GRAPESJS_DEFAULT_HTML', 'django_grapesjs/default.html')


MIN = 'min'
BASE = 'base'

# Use this dictionary to override or add editor configurations
REDACTOR_CONFIG = {
    MIN: 'django_grapesjs/redactor_config/min.html',
    BASE: 'django_grapesjs/redactor_config/base.html',
    **getattr(settings, 'REDACTOR_CONFIG', {})
}

STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')

