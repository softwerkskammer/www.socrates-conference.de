from django.db import models
from django.contrib.auth.models import User

from social_auth.signals import socialauth_registered
from gatekeeper.mail import send_moderation_notices


def new_users_handler(sender, user, response, details, **kwargs):
    user.is_active = False
    send_moderation_notices(user)
    return False

socialauth_registered.connect(new_users_handler, sender=None)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    location = models.CharField(max_length=255, blank=True)
    profession = models.CharField(max_length=255, blank=True)
    focus = models.CharField(max_length=255, blank=True)
    twitter_name = models.CharField(max_length=40, blank=True)
    blog_url = models.URLField(blank=True, verify_exists=False)