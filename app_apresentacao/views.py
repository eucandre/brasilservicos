# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import FormContato

def apresenta(request):
  if request.method == 'POST':
    form  = FormContato(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = FormContato()
  return render(request, "home_page/index.html", {'form':form})
