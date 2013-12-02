===============================
django-blarg
===============================

.. image:: https://badge.fury.io/py/django-blarg.png
    :target: http://badge.fury.io/py/django-blarg
    
.. .. image:: https://travis-ci.org/pydanny/django-blarg.png?branch=master
..         :target: https://travis-ci.org/pydanny/django-blarg

.. image:: https://pypip.in/d/django-blarg/badge.png
        :target: https://crate.io/packages/django-blarg?version=latest


Django 404 and 500 pages the blarg way.

Like https://github.com/404 and https://github.com/500, but for Django.

* Free software: BSD license
* Documentation: http://django-blarg.rtfd.org.

Warnings
--------

* Not yet tested in production anywhere.
* No tests yet!

Usage
-----

Get the package:

.. code-block:: python

    pip install django-blarg

Wire into your project's root URLConf:

.. code-block:: python

    from blarg import error_500, error_404
    
    urlpatterns += patterns("",
        url(r"^500$", error_500, name="error_500"),
        url(r"^404$", error_404, name="error_404"),
    )

Fire up the Django test server

.. code-block:: python

    python manage.py runserver

Test it out!

    * http://127.0.0.1:8000/404
    * http://127.0.0.1:8000/500

Troubleshooting
---------------

You probably already have them, but you'll need 500.html and 404.html templates in the the root of a templates directory.

Features
--------

* The 500 error template is 100% isolated from Django's template mechanisms.
* Works with Django 1.0 upwards. Maybe for earlier, test it and see!
* Works with every version of Python ever supported by Django.
* Works on every HTTP method.

Support this Epic Project
-------------------------

* Submit issues and pull requests
* Donate via gittip: https://gittip.com/pydanny
* Donate via coinbase: https://coinbase.com/checkouts/fcb91011b44028b9cfe96207eecb3bcf
* Donate bitcoins: **14nScLtnipMmQEutCaRiVPWEw9rVm4pUnG**
