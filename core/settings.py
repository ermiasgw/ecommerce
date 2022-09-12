import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-fx+qc#gnbyrat6)3z7wkz&4d8*db(#8%z1aqs5za7470(7sn+h'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'store.apps.StoreConfig',
    'basket',
    'django_countries',
    'payment',
    'orders',

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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.catagories',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

os.environ.setdefault('STRIPE_PUBLISHABLE_KEY', 'pk_test_51LcNtRFmb88Byii1yJ8InJ8iIW5gjDfk6thR4X7OR495Zjc9QLVAxBWxBbqSxDAEUG1UW9DjyBFUttwuyJjqVJ2O00uRyC29DN')
STRIPE_SECRET_KEY = 'sk_test_51LcNtRFmb88Byii15MakOqYLeptq4xOVj67sfEt8sDLAAod7GL5L98oqVpFP2j8OTxAR1uWhXpogkRQvUSRHfncW00WEmefo17'

AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STRIPE_ENDPOINT_SECRET = 'whsec_280bebaa80dcb7c4068a165778fab581fb0da1d593d0d9d1431a214aa776bfa0'