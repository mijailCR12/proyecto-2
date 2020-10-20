from django.db import models

# Create your models here.


class Servicio(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    duracion = models.CharField(max_length=45)
    costo = models.CharField(max_length=45)
