# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_pagamento.models import *
from app_consultor.models import *

class Rateio(models.Model):
  associado = models.ForeignKey(pagamento)
  consultor = models.CharField(max_length = 50)
  valor = models.FloatField()
  
  def __unicode__(self):
    return self.associado.valor

  def save(self, *args, **kwargs):
    if self.associado.pagos == 1:
      self.valor = 24.99*0.4
    
    elif self.associado.pagos > 1:
      self.valor = 24.99*0.02
    
    super(Rateio, self).save(*args, **kwargs)