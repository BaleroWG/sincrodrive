 # -- coding: utf-8 --
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q #para OR en consultas
from .models import ProcesoCopia
import os
import subprocess
from datetime import datetime

CARPETATEMP = 'c:\\temp\\sincrodrive\\'

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView
fields = ('nombre')

from .models import ProcesoCopia


class ProcesoCopiaListar(ListView):
	model = ProcesoCopia
	paginate_by = 10
	context_object_name = 'procesocopia_list'
	
	def get_queryset(self):
		return ProcesoCopia.objects.all()


def procesocopia_correr(request, idproceso):
	procesocopia = ProcesoCopia.objects.get(id=idproceso)
	comandocopia = 'robocopy "{0}" "{1}" {2} {3} /log:"{4}" '
	"""
	{3}= /s /r:2 /w:3
	/s copia subdirectorios si no están vacios
	/r:n n reintentos hasta terminar con error
	/w:t tiempo de espera entre reintentos 
	/log:<ruta>  ruta de archivo de log
	"""
	for procesoactividad in procesocopia.procesoactividad_set.all():
		ahorastr = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
		archivolog = CARPETATEMP + procesocopia.nombre+'_'+procesoactividad.nombre+ahorastr+ '.txt'
	
		comandoEjecutar = comandocopia.format(procesoactividad.rutaorigen, #{0}
												procesoactividad.rutadestino, #{1}
												procesoactividad.extensiones, #{2}
												procesoactividad.parametros, #{3}
												archivolog) #{4}
		#os.system(comandoEjecutar)
		subprocess.call(comandoEjecutar, shell=False)
		print comandoEjecutar

	mensaje = 'Proceso {0} Ejecutado'.format(idproceso)
	return HttpResponse(mensaje)


