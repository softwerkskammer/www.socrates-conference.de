from django.db import models
from django.contrib.auth.models import User
from social_auth.signals import socialauth_registered, pre_update
from gatekeeper.mail import send_moderation_notices
from social_auth.backends.twitter import TwitterBackend
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def new_users_handler(sender, user, response, details, **kwargs):
    user.is_active = False
    send_moderation_notices(user)
    return False

socialauth_registered.connect(new_users_handler, sender=None)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

def twitter_extra_values(sender, user, response, details, **kwargs):
    print response
    profile = user.get_profile()
    profile.twitter_name = response.get("screen_name")
    profile.blog_url = response.get("url") or ""
    profile.location = response.get("location") or ""
    profile.save()
    return True

pre_update.connect(twitter_extra_values, sender=TwitterBackend)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    location = models.CharField(max_length=255, blank=True)
    profession = models.CharField(max_length=255, blank=True)
    focus = models.CharField(max_length=255, blank=True)
    twitter_name = models.CharField(max_length=40, blank=True)
    blog_url = models.URLField(blank=True, verify_exists=False)