from django.db import models
from usuarios.models import Usuario


class Encuesta(models.Model):
    nombre = models.CharField(max_length=100, null=True, default=None)
    destinatario_usuario_id = models.IntegerField()

    class Meta:
        db_table = 'encuesta'

    def __unicode__(self):
        return self.nombre


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=100, null=True, default=None)
    encuesta = models.ForeignKey(Encuesta)
    tipo = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 'preguntas'

    def __unicode__(self):
        return self.pregunta


class Opciones(models.Model):
    opcion = models.CharField(max_length=100, null=True, default=None)
    pregunta = models.ForeignKey(Pregunta)

    class Meta:
        db_table = 'opciones'

    def __unicode__(self):
        return self.opcion


class Respuesta(models.Model):
    solucion = models.CharField(max_length=100, null=True, default=None)
    pregunta = models.ForeignKey(Pregunta)
    opcion = models.ForeignKey(Opciones)
    usuario = models.ForeignKey(Usuario)

    class Meta:
        db_table = 'respuestas'

    def __unicode__(self):
        return self.solucion