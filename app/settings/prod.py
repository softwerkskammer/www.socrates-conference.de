from __future__ import absolute_import
from .base import *

from bundle_config import config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['postgres']['database'],
        'USER': config['postgres']['username'],
        'PASSWORD': config['postgres']['password'],
        'HOST': config['postgres']['host'],
    }
}

MEDIA_ROOT = config['core']['data_directory']

DEFAULT_FROM_EMAIL = 'Ask SoCraTes <ask@socrates-conference.de>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ask@socrates-conference.de'
EMAIL_PORT = 587


DEBUG = False
TEMPLATE_DEBUG = DEBUG
SOCIAL_AUTH_RAISE_EXCEPTIONS = DEBUG

##### defined in settings.keys
### EMAIL_HOST_PASSWORD 
### SECRET_KEY
### TWITTER_CONSUMER_KEY
### TWITTER_CONSUMER_SECRET

