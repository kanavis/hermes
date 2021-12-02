FROM python:3.10
WORKDIR /app
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY backend/ /app
RUN cat /app/hermes/settings.production.template.py | \
    sed -e 's/%%DJANGO_SECRET%%/A{sicjha8shc(UABsv8a7pbsv89bA(SVc8bna98vnbpa9n8scpansc/' | \
    sed -e 's/%%DB_PASSWORD%%/3n9Km2PS9aowaaVa/' \
    > /app/hermes/settings.py
CMD python ./manage.py runserver 0.0.0.0:5000
