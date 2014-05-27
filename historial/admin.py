from django.contrib import admin
from models import Report

# Register your models here
class list_report(admin.ModelAdmin):
	lista = ('comentario', 'fecha',)

admin.site.register(Report, list_report)
