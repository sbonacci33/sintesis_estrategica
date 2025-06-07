from django.urls import path
from . import views

urlpatterns = [
    # Página inicial e institucional
    path("", views.home, name="home"),
    path("sobre-sintesis/", views.sobre_sintesis, name="sobre_sintesis"),

    # Informes
    path("crear/", views.InformeCreateView.as_view(), name="crear_informe"),
    path("informes/", views.InformeListView.as_view(), name="listar_informes"),
    path("informe/<int:informe_id>/", views.InformeDetailView.as_view(), name="detalle_informe"),
    path("informe/<int:informe_id>/editar/", views.InformeUpdateView.as_view(), name="editar_informe"),
    path("informe/<int:informe_id>/eliminar/", views.InformeDeleteView.as_view(), name="eliminar_informe"),
    path("buscar/", views.buscar_informes, name="buscar_informes"),

    # Perfil y cuenta
    path("perfil/", views.ver_perfil, name="ver_perfil"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
    path("perfil/cambiar-clave/", views.CambioPasswordView.as_view(), name="mi_cambio_clave"),

    # Medios
    path("medios/", views.MedioAmigoListView.as_view(), name="medios"),
    path("medios/cargar/", views.MedioAmigoCreateView.as_view(), name="crear_medio"),

    # Suscripciones y servicios
    path("consulta-ia/", views.consulta_ia, name="consulta_ia"),
    path("suscribirse/", views.suscribirse, name="suscribirse"),
]
