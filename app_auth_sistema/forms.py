# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms
from random import choice

from .models import MyUser, Recupera_Senha, Documentos


class CustomUserCreationForm(UserCreationForm):
  nome_usuario = forms.CharField(label = '',max_length = 250,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':u'Nome do Usuário'}))
  email = forms.EmailField(label ='' ,widget = forms.EmailInput(attrs = {'class':'form-control', 'placeholder':u'E-mail'}))
  cpf = forms.CharField(label = '',max_length = 14,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':u'CPF'}))
  id_consultor = forms.CharField(label = '',max_length = 7,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':u'Id do consultor'}))
  
  class Meta:
    model = MyUser
    fields = ['nome_usuario', 'email', 'cpf','id_consultor']



