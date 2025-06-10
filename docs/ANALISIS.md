# Análisis del proyecto

Este documento resume los objetivos y características de **Síntesis Estratégica**.

## Propósito

Plataforma institucional orientada a publicar informes y contenidos de análisis de consumo, con opciones de suscripción y comentarios.

## Funcionalidades implementadas

- Carga, edición y eliminación de informes.
- Búsqueda por título, resumen o autor.
- Suscripción de usuarios.
- Comentarios en informes.
- Consulta a IA (opcional, requiere `OPENAI_API_KEY`).

## Ajustes técnicos

- Modelos con índices para optimizar consultas.
- Vistas basadas en clases y funciones.
- Formularios de Django y validaciones.
- Uso de plantillas con herencia para la interfaz.

## Ejecución de pruebas

```bash
python manage.py test
```
