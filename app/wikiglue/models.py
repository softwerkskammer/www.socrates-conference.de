import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission

from wakawaka.models import Revision

from wikiglue.mail import send_wiki_notification


logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def add_wiki_permissions(sender, instance, created, **kwargs):
    """This signal handler makes sure, that every user who registers has the right to CRUD wiki 
    pages 
    """
    logger.info("Receiving pre_save for user %s" % instance)
    if not instance.has_perm('change_wikipage'):
        try:
            wiki_chg = Permission.objects.get(codename="change_wikipage")
            wiki_add = Permission.objects.get(codename="add_wikipage")
            wiki_del = Permission.objects.get(codename="delete_wikipage")
            rev_chg = Permission.objects.get(codename="change_revision")
            rev_add = Permission.objects.get(codename="add_revision")
            rev_del = Permission.objects.get(codename="delete_revision")
            instance.user_permissions.add(wiki_chg, wiki_add, wiki_del, rev_chg, rev_add, rev_del)
        except Permission.DoesNotExist:
            # this may happen during an inital "createsuperuser" during "syncdb"
            pass


@receiver(post_save, sender=Revision)
def send_wiki_changes_notifications(sender, instance, created, **kwargs):
    """
    Sends a mail if a wiki page is edited (which actually means, 'when a revision
    is created'), to all users which have the field 'notify_recent_changes' set to True in their
    user profile. 
    """
    logging.info("Receiving post_save for revision %s" % instance)

    # Revision objects are only relevant to us, when created (as every rev represents a page edit)
    if created:
        # looks sth like this [(u'mail@example.com',), (u'foo@example.com',)]
        emails = User.objects.filter(userprofile__notify_recent_changes=True).values_list('email')
        send_wiki_notification([tupl[0] for tupl in emails], instance)
