import os
import dj_database_url
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['https://sanghubazar.ondigitalocean.app']


DATABASES = {
    'default': dj_database_url.config()
}
