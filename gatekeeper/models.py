from django.db import models
from django.contrib.auth.models import User
from gatekeeper.mail import send_moderation_notices
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import logging


logger = logging.getLogger(__name__)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        logger.debug('Creating profile for new user "%s".' % instance.username)
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    location = models.CharField(max_length=255, blank=True)
    profession = models.CharField(max_length=255, blank=True)
    focus = models.CharField(max_length=255, blank=True)
    twitter_name = models.CharField(max_length=40, blank=True)
    blog_url = models.URLField(blank=True)
    notify_recent_changes = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'<UserProfile "%s"' % self.__dict__
