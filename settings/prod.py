from __future__ import absolute_import
import os
from .base import *

from postgresify import postgresify

DATABASES = postgresify()

DEFAULT_FROM_EMAIL = 'Ask SoCraTes <ask@socrates-conference.de>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ask@socrates-conference.de'
EMAIL_PORT = 587


DEBUG = False
TEMPLATE_DEBUG = DEBUG
SOCIAL_AUTH_RAISE_EXCEPTIONS = DEBUG

TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
SECRET_KEY = os.environ['SECRET_KEY']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
