#!/usr/bin/env bash

# Instalar dependencias
pip install -r requirements.txt

# Migraciones y archivos estáticos
python manage.py migrate
python manage.py collectstatic --noinput
