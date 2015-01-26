from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from incidencias.models import *
from django.utils import simplejson

def stats(request):
    categorias_all                 = Categoria.objects.all()
    estados_all                    = Estado.objects.all()
    incidencias                    = Incidencia.objects.filter(estado=1)
    incidencias_info               = Incidencia_info.objects.filter(incidencia=incidencias).distinct()
    template = "estadistica.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))


def data_stats(request):
    categoria = int(request.GET['categoria'])
    resultado = []
    incidencias = Incidencia.objects.filter(categoria_id = categoria)
    for ind in incidencias:
    	resultado.append(ind.estado_id)

    message = simplejson.dumps(resultado)
    return HttpResponse(message, content_type='application/json')
