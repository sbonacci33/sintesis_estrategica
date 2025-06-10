# 🧠 Síntesis Estratégica

Este es un proyecto desarrollado como entrega final del curso **Python Flex de Coderhouse**. Se trata de una plataforma profesional construida con **Django**, orientada al análisis de contenidos y estrategias de comunicación digital.

---

## 📌 Descripción del proyecto

**Síntesis Estratégica** es un observatorio digital que permite visualizar, administrar y publicar informes estratégicos, mostrando al mismo tiempo la trayectoria del autor, sus herramientas, metodología y experiencia aplicada.

En esta versión final, se integran:

- Herencia de templates y diseño responsive (Bootstrap).
- Login, registro y edición de perfiles de usuario.
- Carga, visualización y administración de informes (PDFs incluidos).
- Página profesional “Sobre mí” con enlaces externos.
- Comentarios en informes.
- Decoradores y mixins para control de acceso.
- Separación clara de apps y funcionalidades.
- Administración completa de modelos vía Django admin.

---

## 🎥 Video de presentación

📹 [Ver video explicativo de la entrega](https://drive.google.com/file/d/1UpI8vFtWXWLK2-oDYRsXdR-Kw2HZPJQT/view?usp=sharing)

---

## 👤 Acceso de evaluación

Superusuario disponible para revisión:

- **Usuario:** `admininvitado`
- **Contraseña:** `admin1234`

Accedé al panel desde `/admin/`.

---

## 🚀 Instalación y uso

1. **Cloná el repositorio** y creá un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Instalá las dependencias** definidas en `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Aplicá las migraciones** y creá un superusuario (opcional):

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Ejecutá el servidor de desarrollo**:

   ```bash
   python manage.py runserver
   ```

5. **Pruebas automáticas**:

   ```bash
   python manage.py test
   ```

---

## 🧱 Estructura del proyecto

El proyecto está organizado en distintas apps de Django:

- **`observatorio/`**  
  Modelo principal (`Informe`), categorías, comentarios, páginas personalizadas.

- **`accounts/`**  
  Registro, login/logout, perfil, edición de perfil, cambio de contraseña.

- **`pages/`**  
  Home, “Sobre mí”, contacto y futuras secciones estáticas.

---

## 🔍 Funcionalidades principales

### Usuarios
- Registro con username, email y contraseña.
- Login/logout seguro.
- Perfil público editable (nombre, avatar, biografía, etc.).
- Cambio de contraseña.

### Informes
- Vista pública de informes con detalles y descarga de PDF.
- Previsualización embebida (iframe).
- Comentarios públicos para usuarios logueados.
- Crear, editar o eliminar (requiere autenticación y permisos).

### Página "Sobre mí"
- Descripción académica y profesional.
- Experiencia aplicada (Cuchá - medio digital).
- Enlaces externos visuales (LinkedIn, Instagram, web).
- Bloques visuales diferenciados con Bootstrap.

### Seguridad
- CSRF activado.
- Permisos con decoradores (`@login_required`) y mixins (`LoginRequiredMixin`).
- Validaciones y mensajes en formularios.

---

## 📁 Repositorio limpio

- `.gitignore` incluye: `__pycache__/`, `db.sqlite3`, `media/`, `.env`.
- Se incluye `requirements.txt` actualizado con todas las dependencias necesarias.
- La base de datos **NO está incluida** en el repositorio.
- Archivos estáticos (`static/`) y templates organizados y reutilizables.

---

## 🧪 Extras implementados

- 3 CBVs (Class-Based Views) funcionales.
- 1 mixin + 1 decorador personalizado.
- Diseño visual cuidado, con estructura clara y responsive.
- Separación estética en secciones (“Sobre mí”, “Síntesis Estratégica”).
- Íconos e interacciones con Bootstrap Icons.

