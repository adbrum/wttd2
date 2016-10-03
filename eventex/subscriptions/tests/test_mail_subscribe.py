'''
Created on //2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
'''
from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Adriano Regis', cpf='12345678901', email='adbrum@outlook.com', phone='966080448')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'adbrum@outlook.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body (self):
        contents = [
            'Adriano Regis',
            '12345678901',
            'adbrum@outlook.com',
            '966080448',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
