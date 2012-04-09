from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User, Group

from gatekeeper import forms
from gatekeeper.user_helpers import user_in_group


class GatekeeperTestCase(TestCase):
    
    def setUp(self):
        self.active_user = User.objects.create_user('bob', 'bob@example.com', 'secret')

        self.inactive_user = User.objects.create_user('alice', 'alice@example.com', 'secret')
        self.inactive_user.is_active = False
        self.inactive_user.save()


class UserHelperTestCase(GatekeeperTestCase):
    
    def test_user_in_group(self):
        """
        """
        groupname = "some groupname"
        grp = Group(name=groupname)
        grp.save()
        self.active_user.groups.add(grp)
        self.active_user.save()
        
        self.assertTrue(user_in_group(self.active_user, groupname), 
                        "User %s should be member of group %s" % (self.active_user, grp))

        self.assertFalse(user_in_group(self.inactive_user, groupname), 
                        "User %s should not be member of group %s" % (self.inactive_user, grp))


class GatekeeperRegistrationFormTest(GatekeeperTestCase):
    test_data = { 
                'username': 'foo',
                'email': 'foo@example.com',
                'first_name': 'Bob',
                'last_name': 'Foo',
                'location': 'Germany',
                'profession': 'Software Dev',
                'password1': 'foo',
                'password2': 'foo' }

    def test_registration_form_unique_username(self):
        """
        Test that ``RegistrationFormUniqueEmail`` validates uniqueness
        of email addresses.

        """
        self.test_data['username'] = 'alice'
        form = forms.GatekeeperRegistrationForm(data=self.test_data)
        self.failIf(form.is_valid())

    def test_registration_form_unique_email(self):
        """
        Test that ``RegistrationFormUniqueEmail`` validates uniqueness
        of email addresses.

        """
        self.test_data['email'] = 'alice@example.com'
        form = forms.GatekeeperRegistrationForm(data=self.test_data)
        self.failIf(form.is_valid())
        self.assertEqual(form.errors['email'], [u"This email address is already in use. Please supply a different email address."])

        self.test_data['email'] = 'foo@example.com'
        form = forms.GatekeeperRegistrationForm(data=self.test_data)
        self.failUnless(form.is_valid(), form.errors)