# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def registra_rateio(request):
  return render(request, "app_rateio/rateia-pagamentos.html")
