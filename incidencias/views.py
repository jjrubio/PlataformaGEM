from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.utils import simplejson
from django.shortcuts import get_object_or_404
from models import *


def mapa_incidencias(request):
    categorias = Categoria.objects.all()
    incidencias = Incidencia.objects.all()
    incidencias_info = Incidencia_info.objects.all()
    template = "mapa_incidencias.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))

def marcadores_sin_revisar(request):
    # message = {"inc_usuario": "", "inc_categoria": "", "inc_coordenada": "", "inc_direccion": "", "inc_comentario": "", "inc_fecha": "", "inc_evidencia": "", "inc_estado": "", "inc_visible": "", }
    if request.is_ajax():
        data = Incidencia_info.objects.all()

        message = []
        for info in data:
            dict_inc = {}
            dict_inc['inc_usuario'] = info.incidencia.reportada_x_usuario.nick
            dict_inc['inc_categoria'] = info.incidencia.categoria.nombre
            dict_inc['inc_coordenada'] = info.coordenadas
            dict_inc['inc_direccion'] = info.direccion
            dict_inc['inc_comentario'] = info.comentario
            dict_inc['inc_fecha'] = "%s" % info.fecha
            dict_inc['inc_evidencia'] = "/%s" % info.imagen_path
            dict_inc['inc_estado'] = info.incidencia.estado
            dict_inc['inc_visible'] = info.incidencia.visible
            message.append(dict_inc)
    else:
        return HttpResponseRedirect("/")
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')

def lista (request):
    incidencias = Incidencia.objects.all()
    incidencias_info = Incidencia_info.objects.all()
    incidencias_opi = Incidencia_opiniones.objects.all()
    template = "incidencia.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))