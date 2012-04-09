from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.template.loader import render_to_string


def send_wiki_notification(recipients, revision):
    """
    """
    if recipients:
        current_site = Site.objects.get_current()
        msg = render_to_string('wikiglue/wiki_change_notification.txt', 
                                { 'site': current_site, 'revision': revision })
        subject = render_to_string('wikiglue/wiki_change_notification_subject.txt', 
                                    { 'site': current_site, 'revision': revision })
        send_mail(subject, msg, settings.DEFAULT_FROM_EMAIL, recipients)
