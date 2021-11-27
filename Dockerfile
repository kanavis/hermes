FROM python:3.10
WORKDIR /app
COPY backend/ /app
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN cat /app/hermes/settings.production.template.py | \
    tr '%%DJANGO_SECRET%%' "A{sicjh-a8shc-(UABsv8a7pbsv-89bA_(SVc8bna98vnbpa9n8scpansc" | \
    tr '%%DB_PASSWORD%%' "3n9Km2PS9aowaaVa" \
    > /app/hermes/settings.py
CMD gunicorn -b 0.0.0.0:5000 hermes/wsgi.py
