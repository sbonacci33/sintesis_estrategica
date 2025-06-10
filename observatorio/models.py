from django.db import models
from django.contrib.auth.models import User



class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre


# Indices para optimizar las búsquedas de informes
class Informe(models.Model):
    titulo = models.CharField(max_length=200, db_index=True)
    autor = models.CharField(max_length=100, db_index=True)
    resumen = models.TextField(db_index=True)
    palabras_clave = models.CharField(max_length=200, blank=True)
    pdf = models.FileField(upload_to="informes_pdf/", blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return self.titulo


# Registro de términos buscados por los usuarios
class ConsultaUsuario(models.Model):
    termino_buscado = models.CharField(max_length=100, db_index=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.termino_buscado


class Suscriptor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_suscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


class Comentario(models.Model):
    """Comentarios dejados por usuarios en los informes."""

    informe = models.ForeignKey(
        Informe, on_delete=models.CASCADE, related_name="comentarios"
    )
    usuario = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"Comentario de {self.usuario.username}"


class MedioAmigo(models.Model):
    """Enlaces o resúmenes de medios externos."""

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    medio = models.CharField(max_length=150)  
    enlace = models.URLField()
    resumen = models.TextField(blank=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "medio amigo"
        verbose_name_plural = "medios amigos"

    def __str__(self):
        return self.titulo
