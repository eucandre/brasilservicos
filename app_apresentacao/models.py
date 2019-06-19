# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class contato(models.Model):
  nome = models.CharField(max_length = 255)
  email = models.EmailField()
  titulo = models.CharField(max_length = 150)
  mensagem = models.TextField()
  data_contato = models.DateField(auto_now = True)
  
  def __unicode__(self):
    return self.nome
  
  class Meta:
    verbose_name_plural = 'Contatos que mantiveram mensagens na home da brasil casas'
