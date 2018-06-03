django_grapesjs
================

A small library allows you to integrate "grapesjs" into django admin


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


Custom Settings
===============

TEMPLATE_NAME = ''

Reference
===============
* `grapesjs`_


.. _`grapesjs`: https://github.com/artf/grapesjs

