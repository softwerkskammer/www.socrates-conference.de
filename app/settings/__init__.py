from __future__ import absolute_import
import os

if 'ENV_PROD' in os.environ:
    from .prod import *
else:
    try:
        from .local import *
    except ImportError:
        from .base import *
