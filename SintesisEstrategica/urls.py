"""
Configuración de URLs para el proyecto SintesisEstrategica.

La lista ``urlpatterns`` enruta las URLs a las vistas. Para más información consultá:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agregá un import:  from my_app import views
    2. Añadí una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agregá un import:  from other_app.views import Home
    2. Añadí una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluir otra configuración de URLs
    1. Importá la función include: from django.urls import include, path
    2. Añadí una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('observatorio.urls')),  # Rutas de la App
]
