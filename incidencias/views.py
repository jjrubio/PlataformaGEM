from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.utils import simplejson
from models import *
from historial.models import Estado, Report
from django.core import serializers


def mapa_incidencias(request):
    categorias = Categoria.objects.all()
    incidencias = Incidencia.objects.all()
    incidencias_info = Incidencia_info.objects.all()
    template = "mapa_incidencias.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))


def get_dictionary_markers(data, num):
    info = Incidencia_info.objects.get(incidencia_id=data.id)
    historial_actual = Report.objects.get(incidencia_id=data.id)
    dict_inc = {}
    dict_inc['inc_code'] = num
    dict_inc['inc_usuario'] = info.incidencia.reportada_x_usuario.nick
    dict_inc['inc_categoria'] = info.incidencia.categoria.nombre
    dict_inc['inc_coordenada'] = info.coordenadas
    dict_inc['inc_direccion'] = info.direccion
    dict_inc['inc_comentario'] = info.comentario
    dict_inc['inc_fecha'] = "%s" % info.fecha
    dict_inc['inc_evidencia'] = "%s" % info.imagen_path
    dict_inc['inc_estado'] = historial_actual.estado.nombre
    dict_inc['inc_visible'] = info.incidencia.visible
    return dict_inc


def marcadores_filtrados(request, type, subtype):
    if request.is_ajax():
        message = []
        if type == '1':
            for cat in range(Categoria.objects.count()+1):
                num = 0
                for data in Incidencia.objects.filter(categoria_id=cat):
                    num = num +1
                    message.append(get_dictionary_markers(data, num))
        if type == '2':
            for cat in range(Categoria.objects.filter(id = subtype).count()+1):
                num = 0
                for data in Incidencia.objects.filter(categoria_id=subtype):
                    num = num +1
                    message.append(get_dictionary_markers(data, num))
        if type == '3':
            for cat in range(Categoria.objects.count()+1):
                num = 0
                for data in Incidencia.objects.filter(estado=subtype):
                    num = num +1
                    message.append(get_dictionary_markers(data, num))
    else:
        return HttpResponseRedirect("/")
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


def lista_categoria_estados (request):
    categorias_all                 = Categoria.objects.all()
    estados_all                    = Estado.objects.all()
    incidencias                    = Incidencia.objects.filter(estado=1)
    incidencias_info               = Incidencia_info.objects.filter(incidencia=incidencias).distinct()
    template = "incidencia.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))


def filtro_mapa(request, type):
    if request.is_ajax():
        message = []
        if (type == '2'):
            filtroType = Categoria.objects.all()
        else:
            filtroType = Estado.objects.all()
        for filtro in filtroType:
            dict_filtro ={}
            dict_filtro['opcion'] = filtro.nombre
            message.append(dict_filtro)
    else:
        return HttpResponseRedirect("/")
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


def filtro_ajax(request):
    id_cat = request.GET['id_cat']
    incidencias_by_categoria = Incidencia.objects.filter(categoria=id_cat)
    #print incidencias_by_categoria
    info_incidencia_categoria = Incidencia_info.objects.filter(incidencia=incidencias_by_categoria)

    data = serializers.serialize('json', info_incidencia_categoria)
    print data
    return HttpResponse(data, mimetype='application/json')
