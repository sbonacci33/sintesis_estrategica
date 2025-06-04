from django.db import models

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
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

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
    """Datos adicionales para los usuarios registrados."""

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    documento = models.CharField(max_length=50)

    def __str__(self):
        return f"Perfil de {self.user.username}"

