# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from add_contrato import contratos
from django.conf import settings
from .forms import *

def cria_contrato(request):
  if request.method == 'POST':
    form = FormContrato(request.POST, request.FILES)
    if form.is_valid():
      
      form.save()
  else:
    form = FormContrato()
  return render(request, 'app_contrato/index.html', {'form':form})
  
