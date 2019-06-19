# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *

def registra_pagamento(request):
  if request.method == 'POST':
    form = FormPagamento(request.POST)
    if form.is_valid():
      form.save()
      if form.save():
        return redirect('/lista-de-usuarios/')
  else:
    form = FormPagamento()
  return render(request,"app_pagamento/registra-pagamento.html", {"form":form})


@login_required
def lista_pagamentos_associado(request, nr_item):
  item = MyUser.objects.get(pk = nr_item)
  lista_pagamentos = pagamento.objects.all().filter(associado__cpf = item.cpf)
  return render(request, 'app_pagamento/lista-pagamentos-associado.html',{'lista':lista_pagamentos,'associado':item})