from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User, Group

from wakawaka.models import WikiPage, Revision


class WikiGlueTestCase(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create_user('bob', 'bob@example.com', 'secret')
        self.user2 = User.objects.create_user('alice', 'alice@example.com', 'secret')


class WikiNotificationTestCase(WikiGlueTestCase):
    
    def setUp(self):
        """
        NOTE:
        This testcase and this functionality is only relevant if the app's user profile class
        provides a "notify_recent_changes" property, which is set to True for those users
        who wish to receive an email upon every change to every wiki page.
        """
        super(WikiNotificationTestCase, self).setUp()
        self.execute_test = 'notify_recent_changes' in self.user1.get_profile().__dict__
        
    def _create_wiki_page(self):
        """
        Shortcut method for testing
        """
        self.page = WikiPage(slug="some slug")
        self.page.save()
        self.rev = Revision(page=self.page, content="Some content", creator_ip="192.1.1.1")
        self.rev.save()

    def _set_notification_flag_for_user(self, usr):
        profile = usr.get_profile()
        profile.notify_recent_changes = True
        profile.save()
        
    def test_send_no_wiki_change_notifications(self):
        """
        Don't send any mails if no user has option set
        """
        self.failUnless(self.execute_test, "App's user profile has no 'notify_recent_changes' field")
        self._create_wiki_page()
        self.assertTrue(len(mail.outbox) == 0, "No mail should have been sent, because no user asked for it")

    def test_send_wiki_change_notifications_on_page_create(self):
        """
        """
        self.failUnless(self.execute_test, "App's user profile has no 'notify_recent_changes' field")

        self._set_notification_flag_for_user(self.user1)
        self._create_wiki_page()
        self.assertTrue(len(mail.outbox) == 1, "One mail should have been sent, after wiki page creation")

    def test_send_wiki_change_notifications_on_page_edit(self):
        """
        """
        self.failUnless(self.execute_test, "App's user profile has no 'notify_recent_changes' field")

        self._create_wiki_page()
        self._set_notification_flag_for_user(self.user1)
        Revision(page=self.page, content="another page", creator_ip="192.1.1.1").save()
        
        self.assertTrue(len(mail.outbox) == 1, "One mail should've been sent after wiki page edit")
