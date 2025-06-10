from django.contrib import admin
from .models import Categoria, Informe, ConsultaUsuario, Suscriptor, PerfilUsuario, Comentario, MedioAmigo

admin.site.register(Categoria)
admin.site.register(Informe)
admin.site.register(ConsultaUsuario)
admin.site.register(Suscriptor)
admin.site.register(PerfilUsuario)
admin.site.register(Comentario)
admin.site.register(MedioAmigo)
