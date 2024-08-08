"""
Django settings for Demo project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(ut#rb_kez795$(((p(4gj+kiy=_w71c^7_96-9bc04q@dsl)-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'usermodule',
    'userservice',
    'knox',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'Demo.urls'

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

WSGI_APPLICATION = 'Demo.wsgi.application'

GRAPH_MODELS ={
'all_applications': True,
'graph_models': True,
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# DB_NAME = env.str('DB_NAME')
# DATABASES = {
#     'default': {
#                 'ENGINE': 'django.db.backends.mysql',
#                 'NAME': 'xray-app',
#                 'USER': 'root',
#                 'PASSWORD':'toor',
#                 'PORT': '3306',
#                 'HOST': '127.0.0.1'
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase1',
        'USER': 'admin',
        'PASSWORD': 'P4ssw0rd!',
        'HOST': 'database-2.cp02qkug8ip9.ap-south-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # React app URL
#     "http://localhost:5173",  # React app URL
#     "http://localhost:5174",  # React app URL
# ]

# Or use this to allow all origins (development only)
CORS_ALLOW_ALL_ORIGINS = True

# Allow credentials (if needed)
CORS_ALLOW_CREDENTIALS = True

# Additional CORS settings (if needed)
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'authorization',
    'content-type',
    'x-csrftoken',
    'x-requested-with',
]
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^https://.*\.netlify\.app$",
# ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Allowed hosts
ALLOWED_HOSTS = ['3.108.224.21']

# CORS settings (if needed)
CORS_ALLOWED_ORIGINS = [
    "https://xraydoc.netlify.app",
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'
import os
MEDIA_ROOT=os.path.join((BASE_DIR),'media')
MEDIA_URL='/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = 'django-426219-6e9148aeda9a.json'
# GOOGLE_DRIVE_STORAGE_MEDIA_ROOT = 'django'