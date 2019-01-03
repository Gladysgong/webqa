"""
Django settings for webqa project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os ,djcelery
#import os
djcelery.setup_loader()
BROKER_URL= 'redis://localhost:6379/3'
BROKER_TRANSPORT = 'redis'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+y!y#j+guc+r8#51yxlx83jrbkbenyegj)1z6$vl)%6s)*cv8@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.134.110.163', 'frontqa.web.sjs.ted', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rbac',
    'polls',
    'fanyi',
    'webqo',
    'webqw',
    'wiki',
    'editor_md',
    'publicEnv',
    'djcelery',
    'kombu.transport.django',
    'mleval',
    'ml',
    'rest_framework',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rbac.middleware.rbac.RbacMiddleware',
]

ROOT_URLCONF = 'webqa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'webqa.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sogowebqa',
        'USER': 'root',
        'PASSWORD': 'Websearch@qa66',
        'HOST': '10.144.120.30',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
        },
    },
    'db_fhz': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'static_check_history',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'datatest01.web.sjs.ted',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
            'isolation_level': None,
        },
    },
}

# use multi-database in django
DATABASE_ROUTERS = ['webqa.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    'db_fhz': 'db_fhz',
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

USE_L10N = False
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = "/search/odin/pypro/static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SESSION_COOKIE_AGE = 1209600
SESSION_PERMISSION_URL_KEY = 'cool'

SESSION_MENU_KEY = 'awesome'
ALL_MENU_KEY = 'k1'
PERMISSION_MENU_KEY = 'k2'

LOGIN_URL = '/login/'

# REGEX_URL = r'^{url}$'

REGEX_URL = r'^{url}'

SAFE_URL = [
    r'/login/',
    '/admin/.*',
    '/index/',
    r'/logout/',
    '/favicon.ico',
    '/upload/.*',
    '/media/.*',
    '/wiki/.*'
]

MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media/')
ImageFormats = ["jpg", "jpeg", "png"]

CELERY_TIMEZONE = TIME_ZONE

OUTPUT_URL = '/ml/outputs/'

OUTPUT_ROOT = os.path.join(BASE_DIR, 'ml/outputs')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'PAGE_SIZE': 10
}
