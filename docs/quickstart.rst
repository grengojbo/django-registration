.. _quickstart:

Quick start guide
=================

Before installing django-registration, you'll need to have a copy of
`Django <http://www.djangoproject.com>`_ already installed. For the
|version| release, Django 1.1 or newer is required.

Basic configuration and use
---------------------------

Once installed, you can add django-registration to any Django-based
project you're developing. The default setup will enable user
registration with the following workflow:

1. A user signs up for an account by supplying a username, email
   address and password.

2. From this information, a new ``User`` object is created, with its
   ``is_active`` field set to ``False``. Additionally, an activation
   key is generated and stored, and an email is sent to the user
   containing a link to click to activate the account.

3. Upon clicking the activation link, the new account is made active
   (the ``is_active`` field is set to ``True``); after this, the user
   can log in.

Note that the default workflow requires ``django.contrib.auth`` to be
installed, and it is recommended that ``django.contrib.sites`` be
installed as well. You will also need to have a working mail server
(for sending activation emails), and provide Django with the necessary
settings to make use of this mail server (consult `Django's
email-sending documentation
<http://docs.djangoproject.com/en/dev/topics/email/>`_ for details).



Setting up URLs
~~~~~~~~~~~~~~~

The :ref:`default backend <default-backend>` includes a Django
``URLconf`` which sets up URL patterns for :ref:`the views in
django-registration <views>`, as well as several useful views in
``django.contrib.auth`` (e.g., login, logout, password
change/reset). This ``URLconf`` can be found at
``registration.backends.default.urls``, and so can simply be included
in your project's root URL configuration. For example, to place the
URLs under the prefix ``/accounts/``, you could add the following to
your project's root ``URLconf``::

    (r'^accounts/', include('registration.backends.default.urls')),

Users would then be able to register by visiting the URL
``/accounts/register/``, login (once activated) at
``/accounts/login/``, etc.


Required templates
~~~~~~~~~~~~~~~~~~

In the default setup, you will need to create several templates
required by django-registration, and possibly additional templates
required by views in ``django.contrib.auth``. The templates requires
by django-registration are as follows; note that, with the exception
of the templates used for account activation emails, all of these are
rendered using a ``RequestContext`` and so will also receive any
additional variables provided by `context processors
<http://docs.djangoproject.com/en/dev/ref/templates/api/#id1>`_.

**registration/registration_form.html**

Used to show the form users will fill out to register. By default, has
the following context:

``form``
    The registration form. This will be an instance of some subclass
    of ``django.forms.Form``; consult `Django's forms documentation
    <http://docs.djangoproject.com/en/dev/topics/forms/>`_ for
    information on how to display this in a template.

**registration/registration_complete.html**

Used after successful completion of the registration form. This
template has no context variables of its own, and should simply inform
the user that an email containing account-activation information has
been sent.

**registration/activate.html**

Used if account activation fails. With the default setup, has the following context:

``activation_key``
    The activation key used during the activation attempt.

**registration/activation_complete.html**

Used after successful account activation. This template has no context
variables of its own, and should simply inform the user that their
account is now active.

**registration/activation_email_subject.txt**

Used to generate the subject line of the activation email. Because the
subject line of an email must be a single line of text, any output
from this template will be forcibly condensed to a single line before
being used. This template has the following context:

``activation_key``
    The activation key for the new account.

``expiration_days``
    The number of days remaining during which the account may be
    activated.

``site``
    An object representing the site on which the user registered;
    depending on whether ``django.contrib.sites`` is installed, this
    may be an instance of either ``django.contrib.sites.models.Site``
    (if the sites application is installed) or
    ``django.contrib.sites.models.RequestSite`` (if not). Consult `the
    documentation for the Django sites framework
    <http://docs.djangoproject.com/en/dev/ref/contrib/sites/>`_ for
    details regarding these objects' interfaces.

**registration/activation_email.txt**

Used to generate the body of the activation email. Should display a
link the user can click to activate the account. This template has the
following context:

``activation_key``
    The activation key for the new account.

``expiration_days``
    The number of days remaining during which the account may be
    activated.

``site``
    An object representing the site on which the user registered;
    depending on whether ``django.contrib.sites`` is installed, this
    may be an instance of either ``django.contrib.sites.models.Site``
    (if the sites application is installed) or
    ``django.contrib.sites.models.RequestSite`` (if not). Consult `the
    documentation for the Django sites framework
    <http://docs.djangoproject.com/en/dev/ref/contrib/sites/>`_ for
    details regarding these objects' interfaces.

Note that the templates used to generate the account activation email
use the extension ``.txt``, not ``.html``. Due to widespread antipathy
toward and interoperability problems with HTML email,
django-registration defaults to plain-text email, and so these
templates should simply output plain text rather than HTML.

To make use of the views from ``django.contrib.auth`` (which are set
up for you by the default URLconf mentioned above), you will also need
to create the templates required by those views. Consult `the
documentation for Django's authentication system
<http://docs.djangoproject.com/en/dev/topics/auth/#django.contrib.auth.views.login>`_
for details regarding these templates.
