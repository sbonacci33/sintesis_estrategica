from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import (
    Comentario,
    Informe,
    MedioAmigo,
    PerfilUsuario,
    Suscriptor,
)


class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = [
            "titulo",
            "resumen",
            "palabras_clave",
            "contenido",
            "categoria",
            "autor",
            "pdf",
        ]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título del informe"}),
            "resumen": forms.Textarea(attrs={"class": "form-control", "placeholder": "Resumen del contenido", "rows": 3}),
            "palabras_clave": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Palabras clave"}
            ),
            "contenido": forms.Textarea(attrs={"class": "form-control", "placeholder": "Texto completo del informe", "rows": 8}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "autor": forms.TextInput(attrs={"class": "form-control", "placeholder": "Autor/a del informe"}),
            "pdf": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class MedioAmigoForm(forms.ModelForm):
    class Meta:
        model = MedioAmigo
        fields = ["titulo", "autor", "medio", "fecha", "enlace"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título"}),
            "autor": forms.TextInput(attrs={"class": "form-control", "placeholder": "Autor"}),
            "medio": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del medio"}),
            "fecha": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "enlace": forms.URLInput(attrs={"class": "form-control", "placeholder": "URL"}),
        }


class SuscriptorForm(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields = ["nombre", "apellido", "email"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "apellido": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Correo electrónico"}),
        }
        error_messages = {
            "email": {
                "invalid": "Ingresá una dirección de correo válida.",
                "unique": "Este correo ya está registrado.",
            },
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(self.error_messages["password_mismatch"], code="password_mismatch")

        try:
            validate_password(password2, self.instance)
        except ValidationError:
            raise ValidationError("Escribí una contraseña que cumpla con los parámetros.")
        return password2


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]
        widgets = {
            "texto": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Escribí tu comentario aquí"})
        }


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ["biografia", "fecha_nacimiento"]
        widgets = {
            "biografia": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Contanos algo sobre vos"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
