"""Vistas principales de la aplicación Observatorio."""

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Informe, Categoria, ConsultaUsuario
from .forms import InformeForm, SuscriptorForm
from django.contrib import messages
from django.db.models import Q


def home(request):
    """Página inicial del sitio."""
    return render(request, 'observatorio/home.html')

class InformeCreateView(LoginRequiredMixin, CreateView):
    """Formulario para crear un nuevo informe."""

    model = Informe
    form_class = InformeForm
    template_name = "observatorio/crear_informe.html"
    success_url = reverse_lazy("listar_informes")
    login_url = "/accounts/login/"

    def form_valid(self, form):
        messages.success(self.request, "✅ Informe guardado con éxito.")
        return super().form_valid(form)

class InformeListView(ListView):
    """Lista todos los informes."""

    model = Informe
    template_name = "observatorio/listar_informes.html"
    context_object_name = "informes"

    def get_queryset(self):
        return (
            Informe.objects.select_related("categoria")
            .all()
            .order_by("-fecha")
        )

def buscar_informes(request):
    """Realiza búsquedas y registra los términos ingresados."""
    resultados = []
    termino = ""
    if request.method == 'GET':
        termino = request.GET.get('termino', '').strip()
        if termino:
            resultados = (
                Informe.objects.select_related('categoria')
                .filter(
                    Q(titulo__icontains=termino)
                    | Q(resumen__icontains=termino)
                    | Q(autor__icontains=termino)
                )
                .order_by('-fecha')
            )

            # Guarda la búsqueda
            ConsultaUsuario.objects.create(termino_buscado=termino)

    return render(
        request,
        'observatorio/buscar.html',
        {'resultados': resultados, 'termino': termino},
    )

def suscribirse(request):
    """Gestiona el formulario de suscripción."""
    if request.method == 'POST':
        form = SuscriptorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ ¡Te suscribiste con éxito!")
            return redirect('home')
    else:
        form = SuscriptorForm()
    return render(request, 'observatorio/suscribirse.html', {'form': form})

class InformeDetailView(DetailView):
    """Detalle de un informe."""

    model = Informe
    template_name = "observatorio/detalle_informe.html"
    context_object_name = "informe"
    pk_url_kwarg = "informe_id"

    def get_queryset(self):
        return Informe.objects.select_related("categoria")


class InformeUpdateView(LoginRequiredMixin, UpdateView):
    """Actualiza un informe existente."""

    model = Informe
    form_class = InformeForm
    template_name = "observatorio/crear_informe.html"
    success_url = reverse_lazy("listar_informes")
    login_url = "/accounts/login/"
    pk_url_kwarg = "informe_id"


class InformeDeleteView(LoginRequiredMixin, DeleteView):
    """Elimina un informe."""

    model = Informe
    template_name = "observatorio/informe_confirm_delete.html"
    success_url = reverse_lazy("listar_informes")
    login_url = "/accounts/login/"
    pk_url_kwarg = "informe_id"
