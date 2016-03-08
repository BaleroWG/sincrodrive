 # -- coding: utf-8 --
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

LONG_RUTA = 255
LONG_NOMBRE = 100
LONG_TEXTOCORTO = 50 

@python_2_unicode_compatible
class ProcesoCopia( models.Model): #Proceso de copia
	#	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=LONG_NOMBRE)
	def __str__(self):
		return self.nombre
		
@python_2_unicode_compatible
class ProcesoActividad( models.Model):
	#id = models.AutoField(primary_key=True)
	procesocopia = models.ForeignKey(ProcesoCopia, on_delete= models.PROTECT)
	nombre = models.CharField(max_length=LONG_NOMBRE)
	rutaorigen = models.CharField(max_length=LONG_RUTA)
	rutadestino = models.CharField(max_length=LONG_RUTA)
	extensiones = models.CharField(max_length=LONG_TEXTOCORTO)
	parametros = models.CharField(max_length=LONG_TEXTOCORTO)
	def __str__(self):
		return self.nombre



