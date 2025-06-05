"""
Configuración ASGI para el proyecto SintesisEstrategica.

Expone la variable ``application`` de nivel de módulo.

Para más información sobre este archivo consultá:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SintesisEstrategica.settings")

application = get_asgi_application()
