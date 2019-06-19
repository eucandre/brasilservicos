# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_auth_sistema.models import *

class Consultor(models.Model):
  associado = models.ForeignKey(MyUser)
  rede=models.CharField(max_length=7)
  
  def __unicode__(self):
    return self.associado.nome_usuario

  def save(self, *args, **kwargs):
    if self.associado.id_consultor :
      self.rede = self.associado.id_consultor
    super(Consultor, self).save(*args, **kwargs)
    
    
  class Meta:
    verbose_name_plural = "Consultores selecionados para o sistema ligados a uma rede"
