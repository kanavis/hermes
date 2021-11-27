FROM python:3.10
WORKDIR /app
COPY backend/ /app
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN cat /tmp/app/hermes/settings.production.template.py | \
    tr '%%DJANGO_SECRET%%' "`cat /run/secrets/db_password`" | \
    tr '%%DB_PASSWORD%%' "`cat /run/secrets/django_secret`" \
    > /app/hermes/settings.py
CMD gunicorn -b 0.0.0.0:5000 hermes/wsgi.py
