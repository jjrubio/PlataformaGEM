from django.contrib import admin
from models import Reporte, Estado

class list_reporte(admin.ModelAdmin):
	lista = ('comentario', 'fecha',)

admin.site.register(Reporte, list_reporte)
admin.site.register(Estado)
