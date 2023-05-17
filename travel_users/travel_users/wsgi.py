"""
<<<<<<<< HEAD:travel_users/wsgi.py
WSGI config for travel_users project.
========
WSGI config for travel_admin project.
>>>>>>>> github/master:travel_admin/wsgi.py

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<<< HEAD:travel_users/wsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_users.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_admin.settings')
>>>>>>>> github/master:travel_admin/wsgi.py

application = get_wsgi_application()
