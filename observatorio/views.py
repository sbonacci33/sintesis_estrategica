"""Vistas principales de la aplicación Observatorio."""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Informe, Categoria, ConsultaUsuario
from .forms import InformeForm, SuscriptorForm
from django.contrib import messages
from django.db.models import Q


def home(request):
    """Página inicial del sitio."""
    return render(request, 'observatorio/home.html')

def crear_informe(request):
    """Crea un nuevo informe con validación de formulario."""
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Informe guardado con éxito.')
            return redirect('crear_informe')  # Redirige a la misma vista
    else:
        form = InformeForm()
    return render(request, 'observatorio/crear_informe.html', {'form': form})

def listar_informes(request):
    """Muestra el listado de informes ordenados por fecha."""
    informes = (
        Informe.objects.select_related('categoria')
        .all()
        .order_by('-fecha')
    )
    return render(request, 'observatorio/listar_informes.html', {'informes': informes})

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

def detalle_informe(request, informe_id):
    """Muestra el detalle de un informe específico."""
    informe = get_object_or_404(
        Informe.objects.select_related('categoria'), id=informe_id
    )
    return render(request, 'observatorio/detalle_informe.html', {'informe': informe})
