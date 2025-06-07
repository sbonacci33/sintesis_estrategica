from django.contrib import admin
from .models import (
    Categoria,
    Informe,
    ConsultaUsuario,
    Suscriptor,
    MedioAmigo,
    Comentario,
    PerfilUsuario,
)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

@admin.register(Informe)
class InformeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "fecha")
    search_fields = ("titulo", "autor", "resumen")
    list_filter = ("categoria", "fecha")

@admin.register(ConsultaUsuario)
class ConsultaUsuarioAdmin(admin.ModelAdmin):
    list_display = ("termino_buscado", "fecha")
    search_fields = ("termino_buscado",)

@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "fecha_suscripcion")
    search_fields = ("nombre", "apellido", "email")

@admin.register(MedioAmigo)
class MedioAmigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha")
    search_fields = ("titulo", "autor")

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "informe", "fecha")
    search_fields = ("usuario__username", "informe__titulo", "texto")

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("user", "fecha_nacimiento")
    search_fields = ("user__username",)
