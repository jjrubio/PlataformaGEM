from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from historial.models import Reporte

# Create your views here.
def show_historial(request):
	estados	    = State.objects.all()
	reportes    = Reporte.objects.all()
	template    = 'historial_incidencia.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))

def show_historial_dates(request):
	estados	    = State.objects.all()
	reportes    = Reporte.objects.all()
	template    = 'historial_rango_fechas.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))

def show_historial_category(request):
	estados	    = State.objects.all()
	reportes    = Reporte.objects.all()
	template    = 'historial_categoria.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))

def show_historial_states(request):
	estados	    = State.objects.all()
	reportes    = Reporte.objects.all()
	template    = 'historial_estado.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))

def show_historial_votes(request):
	estados	    = State.objects.all()
	reportes    = Reporte.objects.all()
	template    = 'historial_votos.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))

def show_historial_id(request, incidencia_id):
	reportes = Reporte.objects.filter(incidencia_id=incidencia_id)
	template = 'historial_incidencia.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))