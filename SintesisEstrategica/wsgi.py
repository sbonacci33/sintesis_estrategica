"""
Configuración WSGI para el proyecto SintesisEstrategica.

Expone la variable ``application`` de nivel de módulo.

Para más información sobre este archivo consultá:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SintesisEstrategica.settings")

application = get_wsgi_application()
