import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", " 127.0.0.1").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.user',
    'apps.contract',
]


REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'apps.user.authentication.JWTAuthentication',
    # ),
    # 'DEFAULT_FILTER_BACKENDS': [
    #     'django_filters.rest_framework.DjangoFilterBackend'
    # ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spk_notifications.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'spk_notifications.wsgi.application'


DATABASES = {
    'default': {
        "ENGINE":   os.environ.get("SQL_ENGINE"),
        "NAME":     os.environ.get("SQL_DATABASE"),
        "USER":     os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST":     os.environ.get("SQL_HOST"),
        "PORT":     os.environ.get("SQL_PORT"),
    },
}

AUTH_USER_MODEL = 'user.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Atyrau'
USE_I18N = True
USE_TZ = True
USE_L10N = True


CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST", "http://localhost:3002").split(",")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "http://localhost:3002").split(",")

CORS_ALLOW_HEADERS = [
    'access-control-allow-origin',
    'authorization',
    "accept",
    "accept-encoding",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_METHODS = [
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'DELETE'
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Основной backend для аутентификации по username и password
]

TOKEN = os.environ.get("TOKEN")
BOT_POLLING = os.environ.get("BOT_POLLING")
IS_LOCAL = os.environ.get("IS_LOCAL")

IS_DEV = os.getenv('IS_DEV', True)

ARCGIS_USERNAME = os.environ.get("ARCGIS_USERNAME")
ARCGIS_PASSWORD = os.environ.get("ARCGIS_PASSWORD")
ARCGIS_CONTRACT_URL = os.environ.get("ARCGIS_CONTRACT_URL")
ARCGIS_URL_FOR_TOKEN = os.environ.get("ARCGIS_URL_FOR_TOKEN")