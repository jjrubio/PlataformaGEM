from django.db import models


class Usuario(models.Model):
    mail = models.CharField(max_length=30, null=True, default=None)
    password = models.CharField(max_length=45, null=True, default=None)
    nick = models.CharField(max_length=45, null=True, default=None)
    votos = models.IntegerField(null=True, default=0)
    reportes = models.IntegerField(null=True, default=0)
    reparadas = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = 'usuario'

    def __unicode__(self):
        return self.nick
