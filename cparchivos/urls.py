from django.conf.urls import patterns, include, url
from .viewprocesocopia import ProcesoCopiaListar, procesocopia_correr
urlpatterns = patterns('',        
    url(r'^procesos/$', ProcesoCopiaListar.as_view(), name='proceso_listar'),
	url(r'^proceso/(?P<idproceso>\d+)/correr$', procesocopia_correr, name='proceso_correr'),
    #url(r'^clientes/crear/$', ClienteCrear.as_view(), name='cliente_crear'),
)