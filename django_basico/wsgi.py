"""
WSGI config for django_basico project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
path = '/home/Cristyan/LojaPython'
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_basico.settings')

application = get_wsgi_application()
