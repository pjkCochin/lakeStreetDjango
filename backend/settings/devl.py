import os

from .common import *
import dj_database_url
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i+acxn5(akgsn!sr4^qgf(^m&*@+g1@u^t@=8s@axc41ml*f=s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

HEROKU_POSTGRESQL_OLIVE_URL='postgres://ticgofmcpioqkt:1UhtkhaKe8y3K7obh5rA05GZXW@ec2-23-21-234-160.compute-1.amazonaws.com:5432/d9v2vscjbc3dgh'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdb',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)



INTERNAL_IPS = ['192.168.56.1']

INSTALLED_APPS += (
    'autofixture',
)


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../../staticfiles')
STATIC_URL = '/staticfiles/'



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, 'build'),
)



# STATICFILES_DIRS.append(
#     os.path.join(BASE_DIR, '../frontend', 'build'),
# )


