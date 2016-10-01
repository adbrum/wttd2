'''
Created on //2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
'''
from django import forms


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')