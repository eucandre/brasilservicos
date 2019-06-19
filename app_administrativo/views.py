# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app_auth_sistema.models import *
from django.contrib.auth.decorators import login_required

@login_required()
def dashboard(request):
  item = MyUser.objects.all()
  return render(request, "app_administrativo/index.html" , {"item":item})


