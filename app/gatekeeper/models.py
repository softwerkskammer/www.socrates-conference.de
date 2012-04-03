from django.db import models

# Create your models here.

from social_auth.signals import socialauth_registered
from gatekeeper.mail import send_moderation_notices

def new_users_handler(sender, user, response, details, **kwargs):
    user.is_active = False
    send_moderation_notices(user)
    return False

socialauth_registered.connect(new_users_handler, sender=None)