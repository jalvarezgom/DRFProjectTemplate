"""
Django settings for drf_template project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from drf_template.environment import Environment
import drf_template.settings.base as BaseSettings

########################
# Variables de entorno #
########################
SECRET_KEY = Environment.env('SECRET_KEY')
DEBUG = Environment.env('DEBUG') == 'True'
BASE_URL = Environment.BASE_URL

# [Application definition]
INSTALLED_APPS = [
    'drf_template',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    # 'actstream', # Audit module
    'django_filters',
    'corsheaders',
    'schema_graph',
    'sequences.apps.SequencesConfig',
    'drf_spectacular',

    'apps.authentication',
    'apps.task',
    'apps.app_1',
    'apps.app_2',
    'apps.app_3',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# [Database]
DATABASES = {
    'default': {
        'ENGINE': Environment.env('DATABASE_ENGINE'),
        'NAME': Environment.env('DATABASE_NAME'),
        'USER': Environment.env('DATABASE_USER'),
        'PASSWORD': Environment.env('DATABASE_PASSWORD'),
        'HOST': Environment.env('DATABASE_HOST'),
        'PORT': Environment.env('DATABASE_PORT'),
    },
}

ALLOWED_HOSTS = ['*']
# CSRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SAMESITE = 'None'
# SESSION_COOKIE_SAMESITE = 'None'

# [Logging]
LOGGING = Environment.LOGGER_CFG

# [Authentication]
# AUTH_USER_MODEL = BaseSettings.AUTH_USER_MODEL
AUTHENTICATION_BACKENDS = (
    # 'django.contrib.auth.backends.RemoteUserBackend', # Authentication based on remote user
    "django.contrib.auth.backends.ModelBackend",  # Authentication based on username and password
)

#######################
# Valores por defecto #
#######################
ROOT_URLCONF = BaseSettings.ROOT_URLCONF
TEMPLATES = BaseSettings.TEMPLATES
WSGI_APPLICATION = BaseSettings.WSGI_APPLICATION

# [Password validation]
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = BaseSettings.AUTH_PASSWORD_VALIDATORS

# [Internationalization]
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = BaseSettings.LANGUAGE_CODE
TIME_ZONE = BaseSettings.TIME_ZONE
USE_I18N = BaseSettings.USE_I18N
USE_TZ = BaseSettings.USE_TZ

# [Static files (CSS, JavaScript, Images)]
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = BaseSettings.STATIC_URL
STATIC_ROOT = BaseSettings.STATIC_ROOT
STATICFILES_DIRS = BaseSettings.STATICFILES_DIRS

# [Default primary key field type]
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = BaseSettings.DEFAULT_AUTO_FIELD
REST_FRAMEWORK = BaseSettings.REST_FRAMEWORK

########################
# Audit Configuration
# If you need to add an auditing or tracking system, you can use the library 'django-activity-stream'.
########################
# ACTSTREAM_SETTINGS = BaseSettings.ACTSTREAM_SETTINGS


########################
# CORS
########################
CORS_ORIGIN_ALLOW_ALL = BaseSettings.CORS_ORIGIN_ALLOW_ALL
CORS_ALLOW_CREDENTIALS = BaseSettings.CORS_ALLOW_CREDENTIALS
CORS_ALLOW_METHODS = BaseSettings.CORS_ALLOW_METHODS
CORS_ALLOW_HEADERS = BaseSettings.CORS_ALLOW_HEADERS
