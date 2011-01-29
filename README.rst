========================
Django user registration
========================

This is a fairly simple user-registration application for Django_,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.2 or newer, but has no
other dependencies.

For installation instructions, see the file "INSTALL" in this
directory; for instructions on how to use this application, and on
what it provides, see the file `quickstart.rst`_ in the "docs/"
directory.

Installation
============

Install into your python path using pip or easy_install::

    pip install django-uni-form
    easy_install django-uni-form

    pip install git+git://github.com/grengojbo/django-registration.git


Required settings
~~~~~~~~~~~~~~~~~


Add to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.sites',
        ...
        'registration',
        'uni_form',
    )

    AUTHENTICATION_BACKENDS = (
        ...
        'registration.auth.EmailModelBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'django.core.context_processors.request',
    )


    ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

Configurations `django-uni-form`_
Once you've done this, run

    ./manage.py syncdb
    ./manage.py migrate

to install the model used by the default setup.

.. _Django: http://djangoproject.com
.. _`django-uni-form`: http://github.com/codekoala/django-uni-form
.. _`quickstart.rst`: http://github.com/grengojbo/django-registration/blob/master/docs/quickstart.rst
