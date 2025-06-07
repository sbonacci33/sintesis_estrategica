"""Vistas principales de la aplicación Observatorio."""

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from decouple import config

from django.conf import settings
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ComentarioForm, CustomUserCreationForm, InformeForm, SuscriptorForm
from .models import (
    Categoria,
    Comentario,
    ConsultaUsuario,
    Informe,
    MedioAmigo,
    PerfilUsuario,
)

@login_required
def ver_perfil(request):
    perfil = getattr(request.user, "perfilusuario", None)
    return render(request, "observatorio/perfil.html", {
        "usuario": request.user,
        "perfil": perfil,
    })


def home(request):
    """Página inicial del sitio."""
    return render(request, "observatorio/home.html")


def sobre_sintesis(request):
    """Muestra información institucional del proyecto."""
    return render(request, "observatorio/sobre_sintesis.html")


def signup(request):
    """Registro de nuevos usuarios."""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            PerfilUsuario.objects.create(user=user)  # ✔️ creación correcta del perfil
            messages.success(request, "✅ Usuario registrado con éxito.")
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def logout_view(request):
    """Cierra la sesión actual y redirige al inicio."""
    logout(request)
    return redirect("home")


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
        return Informe.objects.select_related("categoria").all().order_by("-fecha")


def buscar_informes(request):
    """Realiza búsquedas y registra los términos ingresados."""
    resultados = []
    termino = ""
    if request.method == "GET":
        termino = request.GET.get("termino", "").strip()
        if termino:
            resultados = (
                Informe.objects.select_related("categoria")
                .filter(
                    Q(titulo__icontains=termino)
                    | Q(resumen__icontains=termino)
                    | Q(autor__icontains=termino)
                )
                .order_by("-fecha")
            )

            # Guarda la búsqueda
            ConsultaUsuario.objects.create(termino_buscado=termino)

    return render(
        request,
        "observatorio/buscar.html",
        {"resultados": resultados, "termino": termino},
    )


def suscribirse(request):
    """Gestiona el formulario de suscripción."""
    if request.method == "POST":
        form = SuscriptorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ ¡Te suscribiste con éxito!")
            return redirect("home")
    else:
        form = SuscriptorForm()
    return render(request, "observatorio/suscribirse.html", {"form": form})


class InformeDetailView(DetailView):
    """Detalle de un informe."""

    model = Informe
    template_name = "observatorio/detalle_informe.html"
    context_object_name = "informe"
    pk_url_kwarg = "informe_id"

    def get_queryset(self):
        return Informe.objects.select_related("categoria")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = self.object.comentarios.select_related("usuario")
        if self.request.user.is_authenticated:
            context["form_comentario"] = ComentarioForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.informe = self.object
                comentario.usuario = request.user
                comentario.save()
                messages.success(request, "Comentario agregado")
        return redirect("detalle_informe", informe_id=self.object.id)


class InformeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Actualiza un informe existente."""

    model = Informe
    form_class = InformeForm
    template_name = "observatorio/crear_informe.html"
    success_url = reverse_lazy("listar_informes")
    login_url = "/accounts/login/"
    pk_url_kwarg = "informe_id"

    def test_func(self):
        return self.request.user.is_superuser


class InformeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Elimina un informe."""

    model = Informe
    template_name = "observatorio/informe_confirm_delete.html"
    success_url = reverse_lazy("listar_informes")
    login_url = "/accounts/login/"
    pk_url_kwarg = "informe_id"

    def test_func(self):
        return self.request.user.is_superuser


class MedioAmigoListView(ListView):
    """Lista de notas y enlaces de medios externos."""

    model = MedioAmigo
    template_name = "observatorio/medios.html"
    context_object_name = "medios"


def consulta_ia(request):
    """Consulta a la IA y devuelve la respuesta."""

    respuesta = None
    if request.method == "POST":
        pregunta = request.POST.get("pregunta")
        if pregunta:
            try:
                completion = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Sos un asistente experto en comunicación y estrategias digitales."},
                        {"role": "user", "content": pregunta},
                    ],
                )
                respuesta = completion.choices[0].message.content
            except Exception as e:
                respuesta = f"⚠️ Error al consultar la IA: {str(e)}"

    return render(request, "observatorio/consulta_ia.html", {"respuesta": respuesta})
