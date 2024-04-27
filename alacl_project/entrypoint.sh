#!/bin/ash

echo "Aplicando migrações do banco de dados"
python manage.py migrate

export APP_PATH="/usr/src/app/"

exec "$@"
