#!/bin/sh

echo "Waiting for postgres..."
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z db 5432; do
      sleep 0.1
    done

echo "PostgreSQL started"
fi

PASSWORD=1234 psql --host db --port 5432 --username=vera --dbname=companie < tracdb/trac.sql
# python manage.py flush --no-input
# python manage.py migrate

exec "$@"

