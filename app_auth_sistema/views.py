# -*- coding: utf-8 -*-
# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.forms import *
from django.views.generic import FormView
from django.http import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class RegistrationView(CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('register')
  template_name = "registration/index.html"

@login_required()
def lista_usuarios(request):
  item = MyUser.objects.all()
  return render(request, "app_auth_sistema/lista-de-usuario.html", {'item':item})

@login_required()
def lista_consultores(request):
  item = MyUser.objects.all().filter(tipo_associado = 'consultor')
  return render(request, "app_auth_sistema/lista-consultores.html",{'item':item})

@login_required()
def lista_minha_rede(request, nr_item):
  item = MyUser.objects.all().filter(id_consultor = nr_item)
  return render(request, "app_auth_sistema/minha-rede.html", {"item":item})

@login_required()
def muda_sernha(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)  # Important!
      messages.success(request, 'Your password was successfully updated!')
      return redirect('change_password')
    else:
      messages.error(request, 'Please correct the error below.')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'accounts/change_password.html', {
    'form': form
  })

# @login_required()
# def acessa_registro_associado(request, nr_item):
#