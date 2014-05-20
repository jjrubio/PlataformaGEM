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
    url(r'^historial_incidencia/', 'historial.views.show_historial', name='history'),
    url(r'^historial_rango_fechas/', 'historial.views.show_historial_dates', name='history_dates'),
    url(r'^historial_categoria/', 'historial.views.show_historial_category', name='history_categ'),
    url(r'^historial_estado/', 'historial.views.show_historial_states', name='history_states'),
    url(r'^historial_voto/', 'historial.views.show_historial_votes', name='history_votes'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
