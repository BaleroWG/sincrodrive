from django.contrib import admin
from .models import ProcesoCopia
from .models import ProcesoActividad

class ProcesoActividadInline(admin.StackedInline): #ProcesoActividadInline(admin.TabularInline)
	model = ProcesoActividad
	extra = 3
	
class ProcesoCopiaAdmin(admin.ModelAdmin):
	inlines= [ProcesoActividadInline]

admin.site.register(ProcesoCopia, ProcesoCopiaAdmin)