FROM python:3.10
WORKDIR /app
COPY backend/ /app
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN cat /app/hermes/settings.production.template.py | \
    tr '%%DJANGO_SECRET%%' "A{sicjha8shc(UABsv8a7pbsv89bA(SVc8bna98vnbpa9n8scpansc" | \
    tr '%%DB_PASSWORD%%' "3n9Km2PS9aowaaVa" \
    > /app/hermes/settings.py
CMD ./manage.py runserver -p 5000
