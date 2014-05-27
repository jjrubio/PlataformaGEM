from django.contrib.auth.models import User
from django.db import models
from incidencias.models import Incidencia


class Report(models.Model):
    fecha           =   models.DateTimeField(null=True, default=None)
    incidencia      =   models.ForeignKey(Incidencia)
    comentario      =   models.CharField(max_length=255)
    usuario_login   =   models.ForeignKey(User, related_name='usuario_login')

    def __unicode__(self):
        return self.comentario

    class Meta:
        db_table = 'reporte'


