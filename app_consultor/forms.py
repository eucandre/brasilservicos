from django import forms
from app_auth_sistema.models import *
from .models import *

class FormClassificaConsultor(forms.ModelForm):

  class Meta:
    model = Consultor
    fields = ('associado',)
