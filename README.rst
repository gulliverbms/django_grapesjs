django_grapesjs
================

.. image:: https://api.codeclimate.com/v1/badges/6b6ca2f03af2d84119c6/maintainability
   :target: https://codeclimate.com/github/gulliverbms/django_grapesjs/maintainability
   :alt: Maintainability

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
        ...

        # or default - if the page is simply static
        html = GrapesJsHtmlField(default=render_to_string('default.html'))

Custom Settings
===============

.. code-block:: python

    # True if you want to save html and css
    GRAPESJS_SAVE_CSS = False  # default value

    # use the value of the field from the db - True, or use the global save editor
    GRAPESJS_DEFAULT_MODELS_DATA = True  # default value

    # redefine the path to the html file, the markup from this file will be used by default
    GRAPESJS_DEFAULT_HTML = 'default.html'  # default value

Reference
===============
* `grapesjs`_


.. _`grapesjs`: https://github.com/artf/grapesjs

