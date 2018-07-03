django_grapesjs
================

.. image:: https://api.codeclimate.com/v1/badges/6b6ca2f03af2d84119c6/maintainability
   :target: https://codeclimate.com/github/gulliverbms/django_grapesjs/maintainability
   :alt: Maintainability

.. image:: https://travis-ci.org/gulliverbms/django_grapesjs.svg?branch=master
   :target: https://travis-ci.org/gulliverbms/django_grapesjs

.. image:: https://coveralls.io/repos/github/gulliverbms/django_grapesjs/badge.svg?branch=master
   :target: https://coveralls.io/github/gulliverbms/django_grapesjs?branch=master

.. image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
   :target: https://github.com/gulliverbms/django_grapesjs/issues
   :alt: contributions welcome

.. image:: http://hits.dwyl.io/gulliverbms/https://github.com/gulliverbms/django_grapesjs.svg
   :target: http://hits.dwyl.io/gulliverbms/https://github.com/gulliverbms/django_grapesjs
   :alt: HitCount


A small library allows you to integrate the page builder "grapesjs" into django admin


Install
=======

.. code-block:: bash

    pip install django_grapesjs


Then add it to your INSTALLED_APPS:

.. code-block:: python

    INSTALLED_APPS = (
        'django_grapesjs',
        ...
        'django.contrib.admin',
    )

To work with the "template_choices", need to add a url-template in the urls.py file

.. code-block:: python

    urlpatterns = [
       path('get_template/', GetTemplate.as_view(), name='dgjs_get_template'),
    ]


Using
===============
Just import the field and add to your model

.. code-block:: python

    from django.db import models
    from django_grapesjs.models import GrapesJsHtmlField


    class ExampleModel(models.Model):
        html = GrapesJsHtmlField()
        ...

        # default_html - path to the html file to display the default value
        # for the field when the form page is received
        html = GrapesJsHtmlField(default_html='default.html')

        # or default - if the page is simply static
        html = GrapesJsHtmlField(default=render_to_string('default.html'))
        ...

        # use the redactor_config argument to select the configuration of the editor
        # Available:
        #     - redactor_config='base' - basic setting, most widgets are used
        #     - redactor_config='min' - minimum setting, only the most necessary
        html = GrapesJsHtmlField(redactor_config='base')
        ...

        # use apply_django_tag = True, if you want to apply render django or jinja tags
        html = GrapesJsHtmlField(default_html='default.html', apply_django_tag=True)
        ...

        # use template_choices to select multiple templates
        html = GrapesJsHtmlField(template_choices=(('django_grapesjs/default.html', 'default'),))

And then inherit "GrapesJsAdminMixin", in the admin class of the current model

.. code-block:: python

    from django.contrib import admin
    from django_grapesjs.admin import GrapesJsAdminMixin


    @admin.register(ExampleModel)
    class ExampleAdmin(GrapesJsAdminMixin, admin.ModelAdmin):
        pass

You can use special tags in your templates, for flexible customization

.. code-block:: HTML

   <ignore></ignore>

If you need to comment out some of the html code during the save,
but execute or display at the time editing in page builder - use this tag.
For example, if your template that uses django or jinja tags does not have any styles or javascript
(because they are in another place, for example, in "footer.html"), you can put css and js in this
tag, styles and javascript code in the editor will work, but when saved and used on the site there
will not be repeating fragments

.. code-block:: HTML

   <hidden></hidden>

If you are editing in the editor with apply_django_tag, you might be distracted by the additional:
{% exclude %}, {% include %}, {% for <expression> %}, etc; - use this tag. He temporarily hides
information, embedded in it during editing, and during the save returns to the original form

Custom Settings
===============

.. code-block:: python

    # True if you want to save html and css
    GRAPESJS_SAVE_CSS = False  # default value

    # use the value of the field from the db - True, or use the global save editor
    GRAPESJS_DEFAULT_MODELS_DATA = True  # default value

    # redefine the path to the html file, the markup from this file will be used by default
    GRAPESJS_DEFAULT_HTML = 'django_grapesjs/default.html'  # default value

    # Add or redefine the configuration of the editor
    REDACTOR_CONFIG = {'base': 'django_grapesjs/redactor_config/base.html'}  # default value


Warning
===============
the library does not work in "inlines"

Reference
===============
* `grapesjs`_


.. _`grapesjs`: https://github.com/artf/grapesjs

