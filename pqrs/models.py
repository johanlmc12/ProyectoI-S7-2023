from django.db import models

# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User


class Solicitud(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=[('P', 'Petición'), ('Q', 'Queja'), ('R', 'Reclamo')])
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']
