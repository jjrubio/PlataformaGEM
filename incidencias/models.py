from django.db import models
from usuarios.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=True, default=None)

    class Meta:
        db_table = 'categorias'

    def __unicode__(self):
        return self.nombre

class Estado(models.Model):
    tipo = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tipo

    class Meta:
        db_table = 'estado'

class Incidencia(models.Model):
    reportada_x_usuario = models.ForeignKey(Usuario)
    categoria = models.ForeignKey(Categoria)
    estado = models.IntegerField(null=True, default=None)
    visible = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 'incidencia'

    # def __unicode__(self):
    #     return self.reportada_x_usuario


class Incidencia_info(models.Model):
    incidencia = models.ForeignKey(Incidencia)
    fecha = models.DateField(null=True, default=None)
    imagen_path = models.ImageField(max_length=120, upload_to='incidencias/', null=True, default=None)
    coordenadas = models.CharField(max_length=50, null=True, default=None)
    direccion = models.CharField(max_length=120, null=True, default=None)
    comentario = models.CharField(max_length=512, null=True, default=None)

    class Meta:
        db_table = 'incidencia_info'

    def __unicode__(self):
        return self.comentario


class Incidencia_opiniones(models.Model):
    incidencia = models.ForeignKey(Incidencia)
    usuario = models.ForeignKey(Usuario)
    voto = models.IntegerField(null=True, default=None)
    comentario = models.CharField(max_length=512, null=True, default=None)

    class Meta:
        db_table = 'Incidencia_opiniones'

    def __unicode__(self):
        return self.comentario
