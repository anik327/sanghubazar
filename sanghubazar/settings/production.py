import os
import dj_database_url
from sanghubazar.settings.development import SECRET_KEY
from .common import *

SECRET_KEY = 'o)kd02_=w%qqeiv81vhkpl6^!*&txmpi#oy$z4-y+)-vdxc&x8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['sanghubazar-api.herokuapp.com']


DATABASES = {
    'default': dj_database_url.config()
}
