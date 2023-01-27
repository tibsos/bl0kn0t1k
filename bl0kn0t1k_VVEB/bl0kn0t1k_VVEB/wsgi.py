import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bl0kn0t1k_VVEB.settings')

application = get_wsgi_application()