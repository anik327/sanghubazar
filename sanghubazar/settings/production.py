import os
import dj_database_url
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG', 'False'] == 'True'


ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')


DATABASES = {
    'default': dj_database_url.parse(os.environ.get["DATABASE_URL"]),
}
