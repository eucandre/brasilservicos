# coding=utf-8
import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
#from simple_history.models import HistoricalRecords
from random import choice
from app_servicos.models import *
from django.contrib.auth.models import User

TIPO_IMOVEL = ((u'casa', 'Casa'), (u'apartamento', 'Apartamento'))

TIPO_ASSOCIADO = ((u'consultor', 'Consultor'), (u'associado', 'Associado'))

class Estado(models.Model):
  nome = models.CharField(max_length = 250)
  
  def __unicode__(self):
    return self.nome
  
  class Meta:
    verbose_name_plural = u"Estados, união federativa"
  
class Cidade(models.Model):
  nome  = models.CharField(max_length = 250)
  estado = models.ForeignKey(Estado)
  
  def __unicode__(self):
    return self.nome
  
  class Meta:
    verbose_name_plural = u"Cidades das Unidades Federativa"
  
class EmailUserManager(BaseUserManager):
  def create_user(self, *args, **kwargs):
    cpf = kwargs["cpf"]
    # email = self.normalize_email(email)
    password = kwargs["password"]
    kwargs.pop("password")
    
    if not cpf:
      raise ValueError(_('Usuarios tem que fornecer cpf.'))
    
    user = self.model(**kwargs)
    user.set_password(password)
    user.save(using = self._db)
    return user
  
  def create_superuser(self, *args, **kwargs):
    user = self.create_user(**kwargs)
    user.is_superuser = True
    user.save(using = self._db)
    return user


class MyUser(PermissionsMixin, AbstractBaseUser):
  id_myuser = models.CharField(max_length = 7, validators=[RegexValidator(r'^\d{0,9}$')])
  image_perfil = models.FileField(upload_to = 'uploads_imagem_profile/%Y/%m/%d/',
                                  verbose_name = _('imagem'),
                                  blank = True,
                                  null = True,
                                  )
  tipo_associado = models.CharField(max_length = 25, choices = TIPO_ASSOCIADO, null = True, blank = True,
                                    default = "associado", editable = True)
  imagem_documentos = models.FileField(upload_to = 'uploads_documentos_usuario/%Y/%m/%d/',
                                verbose_name = _('imagens dos documentos do associado'),
                                )
  email = models.EmailField(
      verbose_name = _('Endereco de email'),blank = True, null = True,
  )
  telefone1 = models.CharField(max_length = 14, verbose_name = _(u'Telefone para contato'))
  telefone2 = models.CharField(max_length = 14, verbose_name = _(u'Telefone para contato'), null = True, blank = True)
  
  nome_usuario = models.CharField(
      verbose_name = _('Nome'),
      max_length = 250,
      blank = False,
      help_text = _('Informe seu nome de usuario'),
  )
  cpf = models.CharField(
      verbose_name = _('CPF'),
      max_length = 14,
      blank = False,
      unique = True,
      help_text = _('Informe seu CPF'),
  )

  rg = models.CharField(
      verbose_name = _('RG'),
      max_length = 50,
      blank = False,
      help_text = _('Informe seu RG'),
  )
  
  tipo_imovel = models.CharField(choices = TIPO_IMOVEL, max_length = 50)
  imagens_imovel = models.FileField(upload_to = 'uploads_imagens_dependencias_imovel/%Y/%m/%d/',
                                       verbose_name = _(u'imagens das dependências do imóvel'),
                                       )
  rua = models.CharField(max_length = 250,verbose_name = _('Rua'),help_text = _('Informe seu nome da sua rua'))
  bairro = models.CharField(max_length = 250,verbose_name = _('Bairro'),help_text = _('Informe seu nome do seu bairro'),)
  
  cidade = models.ForeignKey(Cidade, null = True)
  
  id_consultor = models.CharField(max_length=7, validators=[RegexValidator(r'^\d{0,9}$')])
  servicos= models.ManyToManyField(Servicos)
 # history = HistoricalRecords()
  
  @property
  def _history_user(self):
    return self.changed_by
  
  @_history_user.setter
  def _history_user(self, value):
    self.changed_by = value
  
  def get_full_name(self):
    return self.cpf
  
  def get_short_name(self):
    return self.nome_usuario.__str__()
  
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = True)
  USERNAME_FIELD = 'cpf'
  objects = EmailUserManager()

  def save(self, *args, **kwargs):
    # if getattr(self, 'id', (len(self.id)>5)):
    # id = self.cpf[:4]
    if len(MyUser.objects.all())!=0 and len(MyUser.objects.all()) < 10:
      self.id_myuser = '000'+str(len(MyUser.objects.all()))
    elif len(MyUser.objects.all())!=0 and len(MyUser.objects.all()) >= 10:
      self.id_myuser = '00'+str(len(MyUser.objects.all()))
    
    elif len(MyUser.objects.all())!=0 and len(MyUser.objects.all()) >= 100:
      self.id_myuser = '0'+str(len(MyUser.objects.all()))
    
    elif len(MyUser.objects.all())!=0 and len(MyUser.objects.all()) >= 1000:
      self.id_myuser = str(len(MyUser.objects.all()))
    
    elif len(MyUser.objects.all())!=0 and len(MyUser.objects.all()) > 9999:
      self.id_myuser = -1
      
    super(MyUser, self).save(*args, **kwargs)
  
  
  class Meta:
    verbose_name_plural = 'Usuarios do sistema'


def gera_senha( ):
  caracters = '0123456789abcdefghijlmnopqrstuwvxz-()*&%$#@!{}[]<>?='
  senha = ''
  for char in xrange(8):
    senha += choice(caracters)
  return senha


class Recupera_Senha(models.Model):
  email = models.EmailField()
  data = models.DateField(auto_now = True)
  codigo = models.CharField(max_length = 8, default = gera_senha)
  
  def __unicode__(self):
    return self.email
  
  class Meta:
    verbose_name_plural = u'Sessões para recuperação de senhas'


class Documentos(models.Model):
  nome = models.CharField(max_length = 150)
  documento = models.FileField(upload_to = 'uploads_documentos_usuario/%Y/%m/%d/',
                               verbose_name = _('documentos'),
                               blank = True,
                               )
  data_criacao = models.DateField(auto_now = True)
  usuario = models.ForeignKey(MyUser, related_name = '+', on_delete = models.CASCADE)
  
  def __unicode__(self):
    return self.nome