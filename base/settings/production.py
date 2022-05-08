from .base import *
import dj_database_url


DEBUG = False
ALLOWED_HOSTS = ['climatecare.herokuapp.com']

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
