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
git clone https://github.com/sbonacci33/sintesis_estrategica.git
cd sintesis_estrategica
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
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

5. **Ejecutá las pruebas automáticas (opcional)**:

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
- Búsqueda por título, resumen o autor.

### Página "Sobre mí"
- Descripción académica y profesional.
- Experiencia aplicada (Cuchá - medio digital).
- Enlaces externos visuales (LinkedIn, Instagram, web).
- Bloques visuales diferenciados con Bootstrap.

---

## ⚙️ Detalles técnicos

- Modelos optimizados con índices en campos de búsqueda.
- Uso de **vistas basadas en clases** (CBVs) para crear, listar, actualizar y borrar objetos.
- Decoradores como `@login_required` para proteger accesos sensibles.
- Un `LoginRequiredMixin` aplicado a CBVs para controlar permisos de edición.
- Formularios personalizados para informes, perfiles y comentarios.
- Validación de formularios con mensajes de éxito o error.
- Uso de `widget_tweaks` para mejorar la estética en formularios.

---

## 🧪 Pruebas automáticas

Las pruebas se ejecutan con:

```bash
python manage.py test
```

Actualmente incluye tests mínimos de modelos y formularios. Se recomienda ampliar cobertura para futuros despliegues.

---

## 📁 Buenas prácticas de repositorio

- `.gitignore` incluye: `__pycache__/`, `db.sqlite3`, `media/`, `.env`.
- La base de datos **NO** está incluida.
- Se incluye `requirements.txt` actualizado.
- Organización clara en `static/`, `templates/` y carpetas de apps.
- Código limpio, modular y comentado.

---

## 🧪 Extras implementados

- 3 vistas basadas en clases (CBVs).
- 1 `LoginRequiredMixin` y 1 decorador personalizado.
- Comentarios funcionales en informes.
- Diseño visual cuidado y mobile-friendly.
- Página "Sobre mí" con secciones diferenciadas visualmente.
- Enlaces externos con íconos de Bootstrap.

---

## 🔐 Seguridad y entorno

- CSRF activo en todos los formularios.
- Variables sensibles pueden definirse en `.env`.
- Si se activa la consulta a IA, se requiere: `OPENAI_API_KEY`.

---

## 📌 Repositorio

📍 GitHub: [https://github.com/sbonacci33/sintesis_estrategica](https://github.com/sbonacci33/sintesis_estrategica)