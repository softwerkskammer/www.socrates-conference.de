"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class RegistrationTest(TestCase):
    urls = 'gatekeeper.urls'
    
    def test_renders_form(self):
        """
        """
        c = Client()
        resp = c.get('/register/')
        self.assertEqual(resp.status_code, 200)
