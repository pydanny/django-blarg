========
Usage
========

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

    * http://127.0.0.1/404
    * http://127.0.0.1/500