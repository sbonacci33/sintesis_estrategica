from django.contrib import admin

from .models import (
    Categoria,
    Comentario,
    ConsultaUsuario,
    Informe,
    MedioAmigo,
    PerfilUsuario,
    Suscriptor,
)

admin.site.register(Categoria)
admin.site.register(Informe)
admin.site.register(ConsultaUsuario)
admin.site.register(Suscriptor)
admin.site.register(PerfilUsuario)
admin.site.register(Comentario)
admin.site.register(MedioAmigo)
