from django.conf import settings
from django.db import models
from api.models import Usuario, Status

class Menu(models.Model):
    descripcion = models.CharField(max_length=255)
    entrada = models.CharField(max_length=255, null=True)
    ensalada = models.CharField(max_length=255, null=True)
    plato_fondo = models.CharField(max_length=255, null=True)
    postre = models.CharField(max_length=255, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    usuario_creacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_menu = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion 