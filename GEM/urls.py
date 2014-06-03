from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GEM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mapa-incidencias/', 'incidencias.views.mapa_incidencias', name='mapa'),
    url(r'^marcadores-sin-revisar/', 'incidencias.views.marcadores_sin_revisar', name='markers_unrevised'),
    url(r'^incidencia/', 'incidencias.views.lista_categoria_estados', name='list'),
    url(r'^filtro-mapa/(?P<type>\d+)/$', 'incidencias.views.filtro_mapa', name='map_filter'),
    url(r'^historial/(?P<incidencia_id>\d+)/$', 'historial.views.show_historial_id', name='historyID'),
    url(r'^filtro_ajax/$', 'incidencias.views.filtro', name='filtro-ajax'), 
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
