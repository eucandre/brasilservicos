# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import timezone

from django.core.files import File
from docx import Document
from django.db import models

from app_auth_sistema.models import *
from docx import Document
from docx.shared import Inches
import sys
from add_contrato import *

class contrato_associado(models.Model):
  data_criacao = models.DateField(auto_now = True)
  associado = models.ForeignKey(MyUser)
  contrato = models.FileField(upload_to = 'contrato/%Y/%m/%d/')
  
  def save(self, *args, **kwargs):
    f =contratos(self.associado.id, self.associado.nome_usuario, self.data_criacao)
    self.contrato.save(self.associado.nome_usuario,File(f))
    
    super(contrato_associado, self).save(*args, **kwargs)

  def __unicode__(self):
    return u" De UTC:{0}".format(self.data_criacao)