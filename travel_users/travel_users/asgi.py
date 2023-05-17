"""
<<<<<<<< HEAD:travel_users/asgi.py
ASGI config for travel_users project.
========
ASGI config for travel_admin project.
>>>>>>>> github/master:travel_admin/asgi.py

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<<< HEAD:travel_users/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_users.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_admin.settings')
>>>>>>>> github/master:travel_admin/asgi.py

application = get_asgi_application()
