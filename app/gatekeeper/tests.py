"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from gatekeeper import forms


class GatekeeperTestCase(TestCase):
    
    def setUp(self):
        self.active_user = User.objects.create_user('bob', 'bob@example.com', 'secret')

        self.inactive_user = User.objects.create_user('alice', 'alice@example.com', 'secret')
        self.inactive_user.is_active = False
        self.inactive_user.save()


class GatekeeperRegistrationFormTest(GatekeeperTestCase):

    def test_registration_form_unique_username(self):
        """
        Test that ``RegistrationFormUniqueEmail`` validates uniqueness
        of email addresses.

        """
        form = forms.GatekeeperRegistrationForm(data={ 'username': 'alice',
                                                        'email': 'alice@example.com',
                                                        'password1': 'foo',
                                                        'password2': 'foo' })
        self.failIf(form.is_valid())

    def test_registration_form_unique_email(self):
        """
        Test that ``RegistrationFormUniqueEmail`` validates uniqueness
        of email addresses.

        """
        form = forms.GatekeeperRegistrationForm(data={ 'username': 'foo',
                                                        'email': 'alice@example.com',
                                                        'password1': 'foo',
                                                        'password2': 'foo' })
        self.failIf(form.is_valid())
        self.assertEqual(form.errors['email'], [u"This email address is already in use. Please supply a different email address."])

        form = forms.GatekeeperRegistrationForm(data={ 'username': 'foo',
                                                        'email': 'foo@example.com',
                                                        'password1': 'foo',
                                                        'password2': 'foo' })
        self.failUnless(form.is_valid())