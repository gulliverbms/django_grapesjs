from django.conf import settings

# Django configurations

# a path to grapes.js library (required)
# it must be of dict type which contains the keys: css, js
# and the appropriate paths to each part of the library
# An each path can be of different type:
# can be an absolute one, which starts with: https://... or /...
# or a relative one which looks like: 'grapesjs/...' (be sure that it's placed there)
GRAPESJS_CORE_ASSETS = settings.GRAPESJS_CORE_ASSETS

GRAPESJS_PLUGIN_ASSETS = getattr(settings, 'GRAPESJS_PLUGIN_ASSETS', {})

# A path to form with grapesjs form field
GRAPESJS_FORM = getattr(settings, 'GRAPESJS_FORM', None)

# path to the html file of the form field. Enter your value for the override
GRAPESJS_TEMPLATE = getattr(settings, 'GRAPESJS_TEMPLATE', 'django_grapesjs/forms/fields/textarea.html')

# A path to model with grapejs model field
GRAPESJS_MODEL = getattr(settings, 'GRAPESJS_MODEL', None)

# use the value of the field from the db - True, or use the global save editor
GRAPESJS_DEFAULT_MODELS_DATA = int(getattr(settings, 'GRAPESJS_DEFAULT_MODELS_DATA', True))

# redefine the path to the demo html file, the markup from this file will be used by default
GRAPESJS_DEFAULT_HTML = getattr(settings, 'GRAPESJS_DEFAULT_HTML', 'django_grapesjs/demo.html')

# Grapes JS Settings

# An ID for html tag container which is used during grapesjs initialisation
GRAPESJS_CONTAINER_ID = getattr(settings, "GRAPESJS_CONTAINER_ID", "grapesjs")

# Store Manager

# A prefix which will be applied to all data properties in request body
GRAPESJS_STORAGE_ID_PREFIX = getattr(settings, 'GRAPESJS_STORAGE_ID_PREFIX', 'gjs_')

# A default set of storage type. By default 'remote' is set
# @see: https://grapesjs.com/docs/modules/Storage.html#setup-remote-storage
GRAPESJS_STORAGE_TYPE = getattr(settings, 'GRAPESJS_STORAGE_TYPE', 'remote')

# A number of user action to be made before saving the template state
GRAPESJS_STEPS_BEFORE_SAVE = int(getattr(settings, 'GRAPESJS_STEPS_BEFORE_SAVE', 5))

# A url which grapes.js library will send a template data to
GRAPESJS_URL_STORE = getattr(settings, 'GRAPESJS_URL_STORE', '')

# An ID for quering an database object
GRAPESJS_MODEL_LOOKUP_FIELD = getattr(settings, 'GRAPESJS_REQUEST_ID_FIELD', 'pk')

# A url which grapes.js library will get a template data from
GRAPESJS_URL_LOAD = getattr(settings, 'GRAPESJS_URL_LOAD', '')

# Enable checking of a storage of remote or local types
GRAPESJS_CHECK_LOCAL = int(bool(GRAPESJS_URL_LOAD) or bool(GRAPESJS_URL_STORE))

# A list of allowed host by CORS policy
GRAPESJS_ALLOWED_ORIGIN_LIST = getattr(settings, 'GRAPESJS_ALLOWED_ORIGIN_LIST', [])

# @DEPRECATED
# True if you want to save html and css
GRAPESJS_SAVE_CSS = int(getattr(settings, 'GRAPESJS_SAVE_CSS', False))


# Templating

MIN = 'min'
BASE = 'base'

# Use this dictionary to override or add editor configurations
REDACTOR_CONFIG = {
    MIN: 'django_grapesjs/redactor_config/min.html',
    BASE: 'django_grapesjs/redactor_config/base.html',
    **getattr(settings, 'REDACTOR_CONFIG', {})
}

TEMPLATE_DIR = getattr(settings, 'TEMPLATE_DIR', 'templates')
STATIC_URL = getattr(settings, 'STATIC_URL', "/static/")

# you can override the name of tags
NAME_IGNORE_TAG = getattr(settings, 'NAME_IGNORE_TAG', 'ignore')
NAME_HIDDEN_TAG = getattr(settings, 'NAME_HIDDEN_TAG', 'hidden')
NAME_RENDER_TAG = getattr(settings, 'NAME_RENDER_TAG', 'render')
NAME_MAKEUP_TAG = getattr(settings, 'NAME_MAKEUP_TAG', 'makeup')

REPLACE_SAVE_IGNORE_TAGS = {
    '<%s>' % NAME_IGNORE_TAG: '{# <%s>' % NAME_IGNORE_TAG,
    '</%s>' % NAME_IGNORE_TAG: '</%s> #}' % NAME_IGNORE_TAG,
}
REPLACE_INIT_IGNORE_TAGS = {
    '{# <%s>' % NAME_IGNORE_TAG: '<%s>' % NAME_IGNORE_TAG,
    '</%s> #}' % NAME_IGNORE_TAG: '</%s>' % NAME_IGNORE_TAG,
}

REPLACE_SAVE_HIDDEN_TAGS = {
    '<div hidden=""><%s>' % NAME_HIDDEN_TAG: '<%s>' % NAME_HIDDEN_TAG,
    '</%s></div>' % NAME_HIDDEN_TAG: '</%s>' % NAME_HIDDEN_TAG,
}
REPLACE_INIT_HIDDEN_TAGS = {
    '<%s>' % NAME_HIDDEN_TAG: '<div hidden=""><%s>' % NAME_HIDDEN_TAG,
    '</%s>' % NAME_HIDDEN_TAG: '</%s></div>' % NAME_HIDDEN_TAG,
}

STRING_HANDLERS = [
    'django_grapesjs.utils.tags.makeup.ApplyMakeupTag',
    'django_grapesjs.utils.tags.render.ApplyRenderTag',
    *getattr(settings, 'STRING_HANDLERS', [])
]