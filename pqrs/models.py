
from django.db import models
from django.contrib.auth.models import User


class tabla_modelo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    prediccion = models.FloatField()
    asunto = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.frase