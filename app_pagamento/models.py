# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_auth_sistema.models import *
from django.utils import timezone

class pagamento(models.Model):
  
  associado = models.ForeignKey(MyUser)
  data_hora_pagamento = models.DateField()
  valor  = models.CharField(max_length = 50, default = "24.99")
  pagos = models.IntegerField()
  
  def __unicode__(self):
    return self.associado.nome_usuario

  def save(self, *args, **kwargs):
    if self.pagos == None:
      self.pagos = len(pagamento.objects.all().filter(associado__cpf = self.associado.cpf))+1
    if self.data_hora_pagamento == None:
      self.data_hora_pagamento = timezone.now()
    super(pagamento, self).save(*args, **kwargs)
    
  class Meta:
    verbose_name_plural = "Pagamentos realizados por associados"
