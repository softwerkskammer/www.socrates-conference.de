from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.template.loader import render_to_string


def send_wiki_notification(recipients, revision):
    """
    """
    if recipients:
        current_site = Site.objects.get_current()
        message = render_to_string('wikiglue/wiki_change_notification.txt', 
                                    { 'site': current_site, 'revision': revision })
        subject = render_to_string('wikiglue/wiki_change_notification_subject.txt', 
                                    { 'site': current_site, 'revision': revision })
        email = EmailMessage(subject, 
                            message, 
                            settings.DEFAULT_FROM_EMAIL,
                            bcc=[u.email for u in recipients],
                            headers={ 'X-Softwerkskammer': 'Rocks'})
        email.send()
