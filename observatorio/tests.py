from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Informe


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
            palabras_clave="prueba",
            categoria=categoria,
        )
        self.assertEqual(str(informe), "Informe de prueba")


class InformeViewsTests(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nombre="Cat", descripcion="Desc")
        self.informe = Informe.objects.create(
            titulo="Título",
            autor="Autor",
            resumen="Resumen",
            palabras_clave="clave",
            categoria=categoria,
        )

    def test_listar_informes_status_code(self):
        response = self.client.get(reverse("listar_informes"))
        self.assertEqual(response.status_code, 200)

    def test_detalle_informe_status_code(self):
        url = reverse("detalle_informe", args=[self.informe.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
