from __future__ import absolute_import
import os
from .base import *

from postgresify import postgresify

DATABASES = postgresify()

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = os.environ['SECRET_KEY']
