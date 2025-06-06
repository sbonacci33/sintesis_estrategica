#!/usr/bin/env python
"""Utilidad de línea de comandos de Django para tareas administrativas."""
import os
import sys


def main():
    """Ejecuta tareas administrativas."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SintesisEstrategica.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en la variable PYTHONPATH? "
            "¿Olvidaste activar un entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
