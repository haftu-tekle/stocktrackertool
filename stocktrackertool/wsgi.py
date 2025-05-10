"""
WSGI config for stocktrackertool project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

import os
import sys
from pathlib import Path

VENV_PATH = Path(__file__).resolve().parent.parent / 'stockenv'
SITE_PACKAGES_PATH = VENV_PATH / 'Lib' / 'site-packages'
sys.path.append(str(SITE_PACKAGES_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocktrackertool.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()"""
import os
import sys
from pathlib import Path

VENV_PATH = Path(__file__).resolve().parent.parent / 'stockenv'
SITE_PACKAGES_PATH = VENV_PATH / 'Lib' / 'site-packages'
sys.path.append(str(SITE_PACKAGES_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')

application = get_wsgi_application()
