"""
Django settings for pypyga project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import yaml
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_PATH = Path(__file__).resolve().parent

with open(os.path.join(BASE_DIR, 'settings.yml')) as f:
    conf = yaml.load(f, Loader=yaml.FullLoader)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-bs60d85-v%+csk-ou+kihz((_0ri#^6gq20s3kwk*90vjus#c_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not conf['production']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'pypy.ga', 'pypy-ga.azurewebsites.net']


# Application definition

INSTALLED_APPS = [
    'account',
    'index',
    'problem',
    'submit',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    INSTALLED_APPS.insert(9, "whitenoise.runserver_nostatic")

ROOT_URLCONF = "pypyga.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_PATH, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pypyga.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if conf['db']['type'] == 'local':
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
elif conf['db']['type'] == 'azure-sql':

    name = conf['db']['name']
    user = conf['db']['user']
    password = conf['db']['password']
    host = conf['db']['host']
    port = int(conf['db']['port'])
    driver = 'ODBC Driver 18 for SQL Server'

    sql_params = f"Driver={{{driver}}};Server=tcp:{host},{port};" \
                 f"Database={name};Uid={user};Pwd={password};Encrypt=yes;" \
                 f"TrustServerCertificate=no;Connection Timeout=30;"

    DATABASES = {
        "default": {
            "ENGINE": 'mssql',

            "NAME": name,
            "USER": user,
            "PASSWORD": password,
            "HOST": host,
            "PORT": port,

            'Trusted_Connection': 'no',
            'OPTIONS': {
                'driver': driver,
                'extra_params': sql_params
            }
        }
    }
else:
    print('Invalid DB type')

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
# STATIC_URL = ".well_known/"
STATIC_ROOT = BASE_DIR / '.staticfiles'
STATICFILES_DIRS = [
    PROJECT_PATH / 'static'
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
