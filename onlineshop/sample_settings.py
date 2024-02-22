from datetime import timedelta
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

REST_AUTH = {
    'USE_JWT': True,
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
}
ADMIN_URL = "admin"
