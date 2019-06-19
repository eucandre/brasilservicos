from django import forms
from .models import *

class FormPagamento(forms.ModelForm):
  associado = forms.ModelChoiceField(queryset = MyUser.objects.all(), widget = forms.Select(attrs = {'class':'form-control'}))
  class Meta:
    model = pagamento
    fields = ('associado','valor',)