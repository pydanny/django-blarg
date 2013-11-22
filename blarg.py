import os

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.shortcuts import render

# Explicitly get the 500 template outside the Django template
#   loading mechanism. We do this so there is absolutely no
#   chance that Django will attempt to do any parsing of this
#   file.
for template_dir in settings.TEMPLATE_DIRS:
    template_name = os.path.join(template_dir, "500.html")
    if os.path.exists(template_name):
        with open(template_name) as f:
            text = f.read()
        break
else:
    msg = "Please add a 500.html to your base templates directory"
    raise ImproperlyConfigured(msg)

def error_500(request):
    # Display 500.html template as a text file, not as a Django template.
    # Written as a Function-Based View so it handles all HTTP methods simply.
    response = HttpResponse(text)
    response.status_code = 500
    return response

def error_404(request):
    # Written as a Function-Based View so it handles all HTTP methods simply.
    response = render(request, "404.html")
    response.status_code = 404
    return response