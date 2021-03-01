from django.conf import settings
from django.db import models
from api.models import Usuario, Menu

class UsuarioMenu(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.id 