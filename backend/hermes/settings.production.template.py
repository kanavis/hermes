from .system_settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%%DJANGO_SECRET%%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hermes',
        'USER': 'hermes',
        'PASSWORD': '%%DB_PASSWORD%%',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}
