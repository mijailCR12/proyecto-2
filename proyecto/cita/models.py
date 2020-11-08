from django.db import models

# Create your models here.


class Empleado(models.Model):
    Nombre = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10)
    Correo = models.CharField(max_length=30)
    Especialidad = models.CharField(max_length=100)
    Ubicacion = models.CharField(max_length=255)
    Edad = models.CharField(max_length=10)

    def __str__(self):
        return self.Nombre


class Servicio(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=255)
    #duracion = models.DateTimeField()
    Duracion = models.CharField(max_length=15)
    Costo = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre


class Cliente(models.Model):
    Nombre = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10)
    Correo = models.CharField(max_length=30)
    Ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.Nombre


class Cita(models.Model):
    detalle = models.CharField(max_length=100)
    #fecha = models.CharField(max_length=50)
    fecha = models.DateField()
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
