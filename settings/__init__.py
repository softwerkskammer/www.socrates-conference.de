from __future__ import absolute_import
import os

if 'ENV_PROD' in os.environ:
    from .prod import *
else:
    try:
        # try to import local settings ...
        from .local import *
    except ImportError:
        # ... and fall back to base settings in case of failure
        from .base import *
        
    try:
        # try local keys ...
        from .local_keys import *
    except ImportError:
        # ... but they are not essential
        pass

