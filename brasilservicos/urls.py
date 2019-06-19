from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app_administrativo.views import *
from app_auth_sistema.views import *
from app_consultor.views import *
from app_pagamento.views import *
from app_rateio_pagamento.views import *
from app_apresentacao.views import *
from app_contrato.views import *

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^dash', dashboard),
    url(r'^$', apresenta),
    url(r'^cria-contrato', cria_contrato),
    url(r'^pagamento', registra_pagamento),#registra o pagamento de cada associado
    #faz a lista de os pagamentos realizados por determinado cliente
    url(r'^registro-pagamentos/(?P<nr_item>\d+)/$', lista_pagamentos_associado, name = "lista_pagamentos_associados"),
    url(r'^classifica-para-consultor/$',classifica_consultor, name = "classifica-consultor"),
    #url(r'^rateio-pagamentos/$',),
    url(r'^lista-de-usuarios',lista_usuarios, name = "lista_usuarios"),
    url(r'^lista-de-consultores',lista_consultores, name = "lista_consultores"),
    url(r'^minha-rede/(?P<nr_item>\d+)/$',lista_minha_rede, name = "lista_minha_rede"),
    #url(r'^minha-rede/$',lista_minha_rede, name = "lista_minha_rede"),
    url(r'^register/$', RegistrationView.as_view(), name = "register"),
    url(r'^edita-password/$', muda_sernha, name='change_password'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
