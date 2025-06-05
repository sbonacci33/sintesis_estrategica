from django.test import TestCase
from django.urls import reverse

from .models import Informe, Categoria, MedioAmigo


class HomeViewTests(TestCase):
    def test_home_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class InformeModelTests(TestCase):
    def test_str_representation(self):
        categoria = Categoria.objects.create(nombre="Prueba", descripcion="Cat")
        informe = Informe.objects.create(
            titulo="Informe de prueba",
            autor="Autor",
            resumen="Resumen",
            contenido="Contenido",
            categoria=categoria,
        )
        self.assertEqual(str(informe), "Informe de prueba")


class MedioAmigoModelTests(TestCase):
    def test_str_representation(self):
        medio = MedioAmigo.objects.create(
            titulo="Nota de prueba", enlace="http://example.com", resumen="Res"
        )
        self.assertEqual(str(medio), "Nota de prueba")
