# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app_auth_sistema.models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def classifica_consultor(request):
  if request.method == 'POST':
    form = FormClassificaConsultor(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormClassificaConsultor()
  return render(request, "app_consultor/classifica-consultor.html",{'form':form})
  
