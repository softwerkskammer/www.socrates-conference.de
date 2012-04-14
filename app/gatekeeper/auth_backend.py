from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)
class EmailModelBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            logger.debug("EMAILBACKEND 2 %s" % user)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None