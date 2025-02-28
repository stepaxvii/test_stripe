import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ Django
SECRET_KEY = 'django-insecure-i9**_wuoysg@!t1as#xo1xoa5!@6_^c2@p0#5dq6w*1)5%(x4#'

# Ключи Stripe
STRIPE_PUBLISHABLE_KEY_USD = os.getenv('STRIPE_PUBLISHABLE_KEY_USD')
STRIPE_SECRET_KEY_USD = os.getenv('STRIPE_SECRET_KEY_USD')

STRIPE_PUBLISHABLE_KEY_EUR = os.getenv('STRIPE_PUBLISHABLE_KEY_EUR')
STRIPE_SECRET_KEY_EUR = os.getenv('STRIPE_SECRET_KEY_EUR')

DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = os.getenv(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost'
).split(',')

ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS]


CSRF_TRUSTED_ORIGINS = os.getenv(
    'CSRF_TRUSTED_ORIGINS',
    default='https://127.0.0.1,https://localhost'
).split(',')

CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in CSRF_TRUSTED_ORIGINS]


INSTALLED_APPS = [
    'items.apps.ItemsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_stripe.urls'

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

WSGI_APPLICATION = 'test_stripe.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/django/static/'
STATIC_ROOT = '/home/django/staticfiles/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
