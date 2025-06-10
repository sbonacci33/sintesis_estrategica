# Análisis del proyecto

Este documento resume las principales características del portal **Síntesis Estratégica** y los ajustes realizados para mantener el código ordenado.

## Funcionalidades

- Gestión de informes con carga, edición y eliminación.
- Búsqueda de informes por título, autor o resumen.
- Suscripción de usuarios mediante formulario validado.
- Consultas a un modelo de IA (opcional, requiere `OPENAI_API_KEY`).
- Administración sencilla de datos desde el panel de Django.

## Ajustes aplicados

- Se registraron todos los modelos en `admin.py` para facilitar la administración.
- Se añadieron pruebas unitarias que validan la lista y el detalle de informes.
- Se aclaró en el README el uso de la variable `OPENAI_API_KEY`.

Para ejecutar las pruebas una vez instaladas las dependencias:

```bash
python manage.py test
```
