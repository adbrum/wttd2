'''
Created on //2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
'''
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))
