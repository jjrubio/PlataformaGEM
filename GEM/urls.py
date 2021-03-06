from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'incidencias.views.mapa_incidencias', name='mapa2'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mapa-incidencias/$', 'incidencias.views.mapa_incidencias', name='mapa'),
    url(r'^marcadores-filtrados/(?P<vtype>\d+)/(?P<vsubtype>\d+)/$', 'incidencias.views.marcadores_filtrados', name='markers_filters'),
    url(r'^incidencia/', 'incidencias.views.lista_categoria_estados', name='list'),
    url(r'^mensaje/$', 'incidencias.views.enviar_mensaje', name='mensaje'),
    url(r'^filtro-mapa/(?P<type>\d+)/$', 'incidencias.views.filtro_mapa', name='map_filter'),
    url(r'^historial/(?P<incidencia_id>\d+)/$', 'historial.views.show_historial_id', name='historyID'),
    url(r'^filtro_tabs/$', 'incidencias.views.filtroTabs', name='filtro-tabs'),
    url(r'^estadisticas/$', 'estadisticas.views.stats', name='stats'),
    url(r'^data_stats/$', 'estadisticas.views.data_stats', name='data_stats'),
    url(r'^update_state/$','incidencias.views.estadoActualizacion', name='update-state'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
