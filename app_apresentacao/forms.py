# coding=utf-8
from django import forms
from .models import contato

class FormContato(forms.ModelForm):
  nome = forms.CharField(max_length = 255, widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Seu nome'}))
  titulo = forms.CharField(max_length = 255,widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Título'}))
  email = forms.EmailField(widget = forms.EmailInput(attrs = {'class':'form-control','placeholder':'email'}))
  mensagem = forms.CharField(widget = forms.Textarea(attrs = {'class':'form-control','placeholder':'Mensagem'}))
  
  class Meta:
    model = contato
    fields = ('nome','titulo', 'mensagem','email')