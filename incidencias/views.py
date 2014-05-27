from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.utils import simplejson
from models import *


def mapa_incidencias(request):
    categorias = Categoria.objects.all()
    incidencias = Incidencia.objects.all()
    incidencias_info = Incidencia_info.objects.all()
    template = "mapa_incidencias.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))

def marcadores_sin_revisar(request):
    if request.is_ajax():
        message = []
        for cat in range(Categoria.objects.count()+1):
            num = 0
            for data in Incidencia.objects.filter(categoria_id=cat):
                info = Incidencia_info.objects.get(incidencia_id=data.id)
                num = num + 1
                dict_inc = {}
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
                message.append(dict_inc)
    else:
        return HttpResponseRedirect("/")
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')
