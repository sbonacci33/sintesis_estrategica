from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.InformeCreateView.as_view(), name='crear_informe'),
    path('informes/', views.InformeListView.as_view(), name='listar_informes'),
    path('buscar/', views.buscar_informes, name='buscar_informes'),
    path('suscribirse/', views.suscribirse, name='suscribirse'),
    path('informe/<int:informe_id>/', views.InformeDetailView.as_view(), name='detalle_informe'),
    path('informe/<int:informe_id>/editar/', views.InformeUpdateView.as_view(), name='editar_informe'),
    path('informe/<int:informe_id>/eliminar/', views.InformeDeleteView.as_view(), name='eliminar_informe'),
]
