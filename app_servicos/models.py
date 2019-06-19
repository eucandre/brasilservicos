# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


ESCOLHA = ((u'SIM', 'SIM'), (u'NAO', 'NÃO'))

class Servicos(models.Model):
  nome = models.CharField(max_length = 250)
  descricao = models.TextField()
  valor = models.FloatField(help_text=u"Valor do serviço")
  
  def __unicode__(self):
    return self.nome
  
  class Meta:
    verbose_name_plural = "Serviços disponíveis na plataforma"
