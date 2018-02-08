"""
WSGI config for pineapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

path = '/Users/chris/src/pineapp/pineapp'

if path not in sys.path:
    sys.path.append(path)

print((sys.path))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pineapp.settings")
application = get_wsgi_application()
