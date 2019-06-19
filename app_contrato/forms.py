from django import forms
from .models import *

class FormContrato(forms.ModelForm):
  class Meta:
    model = contrato_associado
    fields = ('associado', )