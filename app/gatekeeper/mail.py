from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.template.loader import render_to_string


def send_moderation_notices(new_user):
    """
    """
    current_site = Site.objects.get_current()

    subject = render_to_string('registration/activation_email_subject.txt', 
                                { 'site': current_site, 'new_user': new_user })
    message = render_to_string('registration/activation_email.txt', 
                                { 'site': current_site, 'new_user': new_user })

    recipients = User.objects.filter(groups__name=settings.GATEKEEPER_MODERATOR_GROUP)
    print "recipients:", recipients
    if recipients:
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [u.email for u in recipients])
    
    return new_user