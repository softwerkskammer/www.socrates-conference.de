from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
import logging


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

