from django.contrib.auth.models import User
from django.db import models

class Estado(models.Model):
    tipo = models.CharField(max_length=20, null=True, default=None)

    def __unicode__(self):
        return self.tipo

    class Meta:
        db_table = 'estado'

class Reporte(models.Model):
    comentario = models.CharField(max_length=255)
    fecha = models.DateTimeField(null=True, default=None)
    incidencia = models.ForeignKey('incidencias.Incidencia')
    estado = models.ForeignKey(Estado)
    usuario_login = models.ForeignKey(User, related_name='usuario_login')

    def __unicode__(self):
        return self.comentario

    class Meta:
        db_table = 'reporte'