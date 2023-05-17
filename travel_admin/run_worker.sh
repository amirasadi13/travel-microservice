# persistent revokes: https://docs.celeryproject.org/en/latest/userguide/workers.html#worker-persistent-revokes
python manage.py makemigrations --noinput
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:8001