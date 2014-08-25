from django.db import models
from usuarios.models import Usuario


class Mensaje(models.Model):
    titulo = models.CharField(max_length=45, null=True, default=None)
    fecha = models.DateTimeField(null=True, default=None)
    cuerpo = models.CharField(max_length=250, null=True, default=None)
    imagen_path = models.ImageField(max_length=250, upload_to='mensajes/', null=True, default=None)
    destinatario_usuario = models.ForeignKey(Usuario)
    visible = models.IntegerField(null=True, default=1)

    class Meta:
        db_table = 'mensajes'

    def __unicode__(self):
        return self.titulo
