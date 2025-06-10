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
            contenido="Contenido",
            categoria=categoria,
        )
        self.assertEqual(str(informe), "Informe de prueba")


class InformeListViewTests(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nombre="Demo", descripcion="Cat")
        Informe.objects.create(
            titulo="Ejemplo",
            autor="Autor",
            resumen="Resumen",
            contenido="Contenido",
            categoria=categoria,
        )

    def test_list_view_status_code(self):
        response = self.client.get(reverse("listar_informes"))
        self.assertEqual(response.status_code, 200)


class InformeDetailViewTests(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nombre="Demo", descripcion="Cat")
        self.informe = Informe.objects.create(
            titulo="Ejemplo",
            autor="Autor",
            resumen="Resumen",
            contenido="Contenido",
            categoria=categoria,
        )

    def test_detail_view_status_code(self):
        response = self.client.get(
            reverse("detalle_informe", kwargs={"informe_id": self.informe.id})
        )
        self.assertEqual(response.status_code, 200)

