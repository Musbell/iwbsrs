"""
Django settings for iwsrs project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url
# import dropbox

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "57mbb)@2$okq7lr-$wl2ydl^!5m1304dbmo%k$*19c5(y&6ad5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [# Third-party apps
    "django_bootstrap_breadcrumbs",'report_builder','crispy_forms','admin_interface','flat_responsive','colorfield',
    'pwa',
    # 'storages',

    ########################
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions',
    'django.contrib.messages',# Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic','django.contrib.staticfiles',

    # Local apps here
    'subscriber.apps.SubscriberConfig','simRegistration.apps.SimregistrationConfig',
    'mobileNetworks.apps.MobilenetworksConfig','mobileNetworkOperator.apps.MobilenetworkoperatorConfig',
    'registrationAgent.apps.RegistrationagentConfig',]

MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware',]

ROOT_URLCONF = 'iwsrs.urls'

# AUTHENTICATION_BACKENDS = [
#     'django_auth0.auth_backend.Auth0Backend',
#     'django.contrib.auth.backends.ModelBackend'
# ]

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [os.path.join(BASE_DIR,'templates')],
    'APP_DIRS': True,'OPTIONS': {'context_processors': [# 'django_auth0.context_processors.auth0',
        'django.template.context_processors.debug','django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages',
        'django.template.context_processors.static','django.template.context_processors.media'],'debug': DEBUG,},},]

WSGI_APPLICATION = 'iwsrs.wsgi.application'

# AUTH0_DOMAIN = 'musbell.auth0.com'
# AUTH0_CLIENT_ID = 'OsuVV94GUBKzZZKkJ3oGwFla4812Au2B'
# AUTH0_SECRET = 'cmvyO2zo38fSBvyD_vOZHXMhZ0TJBjtXjBug4awk1ib-ThbComBZ3AHdNBR1IbKY'
# AUTH0_CALLBACK_URL = 'http://localhost:8000/sim_reg/add_subscriber_sim_detail/'
# AUTH0_SUCCESS_URL = 'http://localhost:8000/sim_reg/add_subscriber_sim_detail/'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR,'db.sqlite3'),}}

AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT,'staticfiles')
STATIC_URL = '/static/'
#
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = [os.path.join(PROJECT_ROOT,'static'),]
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Point the AbstractUser to AUTH_USER_MODEL from subscriber model
AUTH_USER_MODEL = 'subscriber.Subscriber'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.SessionAuthentication',)}

BREADCRUMBS_TEMPLATE = "django_bootstrap_breadcrumbs/bootstrap4.html"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

PWA_APP_NAME = 'IWBSRS'
PWA_APP_DESCRIPTION = "Integrated Web Based Sim Registration System"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [{'src': '/static/assets/img/favicon.ico','sizes': '160x160'}]

# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
#
# DROPBOX_OAUTH2_TOKEN = '7fQ61jR3jOQAAAAAAAAGPVD-v59rhVA1guPfI2n8Tt6IC95unYmGpQJvMOVMOQS_'
# DROPBOX_ROOT_PATH = 'ISRS'

#07035226032