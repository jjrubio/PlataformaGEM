from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.utils import simplejson
from models import *
from historial.models import Estado, Reporte
from django.core import serializers


def mapa_incidencias(request):
    categorias = Categoria.objects.all()
    incidencias = Incidencia.objects.all()
    incidencias_info = Incidencia_info.objects.all()
    template = "mapa_incidencias.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))


def get_dictionary_markers(data, num):
    info = Incidencia_info.objects.get(incidencia_id=data.id)
    dict_inc = {}
    print info
    dict_inc['inc_code'] = num
    dict_inc['inc_usuario'] = info.incidencia.reportada_x_usuario.nick
    dict_inc['inc_categoria'] = info.incidencia.categoria.nombre
    dict_inc['inc_coordenada'] = info.coordenadas
    dict_inc['inc_direccion'] = info.direccion
    dict_inc['inc_comentario'] = info.comentario
    dict_inc['inc_fecha'] = "%s" % info.fecha
    dict_inc['inc_evidencia'] = "%s" % info.imagen_path
    dict_inc['inc_estado'] = info.incidencia.estado.tipo
    dict_inc['inc_visible'] = info.incidencia.visible
    return dict_inc


def marcadores_filtrados(request, vtype, vsubtype):
    if request.is_ajax():
        message = []
        if vtype == '1':
            for cat in range(Categoria.objects.count()+1):
                num = 0
                for data in Incidencia.objects.filter(categoria_id=cat):
                    num = num +1
                    message.append(get_dictionary_markers(data, num))
        if vtype == '2':
            for cat in range(Categoria.objects.filter(id=vsubtype).count()+1):
                num = 0
                for data in Incidencia.objects.filter(categoria_id=vsubtype):
                    num = num +1
                    message.append(get_dictionary_markers(data, num))
        if vtype == '3':
            for cat in range(Categoria.objects.count()+1):
                num = 0
                for data in Incidencia.objects.filter(estado=vsubtype):
                    num = num +1
                    message.append(get_dictionary_markers(data, num))
    else:
        return HttpResponseRedirect("/")
    json = simplejson.dumps(message)
    return HttpResponse(json, content_type='application/json')


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
            for filtro in filtroType:
                dict_filtro ={}
                dict_filtro['opcion'] = filtro.nombre
                message.append(dict_filtro)
        else:
            filtroType = Estado.objects.all()
            for filtro in filtroType:
                dict_filtro ={}
                dict_filtro['opcion'] = filtro.tipo
                message.append(dict_filtro)
    else:
        return HttpResponseRedirect("/")
    json = simplejson.dumps(message)
    return HttpResponse(json, content_type='application/json')


def filtroTabSelec(request):
    id_estado = request.GET['id_estado']
    id_cat = request.GET['id_cat']

    incidencias_by_categoria_by_estado = Incidencia.objects.filter(categoria=id_cat).filter(estado=id_estado)
    info_incidencia_categoria_estado = Incidencia_info.objects.filter(incidencia=incidencias_by_categoria_by_estado)

    data = serializers.serialize('json', info_incidencia_categoria_estado)
    print data
    return HttpResponse(data, content_type='application/json')

def filtroTabs(request):
    id_estados = request.GET['id_estados']
    result = []
    datos = {}

    incidencias_by_estado = Incidencia.objects.filter(estado=id_estados)
    info_incidencia_estado = Incidencia_info.objects.filter(incidencia=incidencias_by_estado)

    for i in info_incidencia_estado:
        datos['id_incidencia'] = i.incidencia.pk
        datos['reportada_x_usuario_incidencia'] = i.incidencia.reportada_x_usuario
        datos['comentario_incidencia'] = i.comentario
        datos['fecha_incidencia'] = i.fecha
        datos['imagen_incidencia'] = i.imagen_path

        result.append(datos)

    #data = serializers.serialize('json',datos)
    data = serializers.serialize('json',info_incidencia_estado)

    return HttpResponse(data, content_type='application/json')
