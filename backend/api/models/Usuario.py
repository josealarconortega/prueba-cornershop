from django.conf import settings
from django.db import models
from api.models import Perfil

class Usuario(models.Model):
    rut = models.CharField(max_length=255, null=True)
    nombre = models.CharField(max_length=255)
    usuario_slack = models.CharField(max_length=255, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    uid =  models.CharField(max_length=255, null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.rut