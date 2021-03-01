from django.db import models

class Perfil(models.Model):
    descripcion = models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion