from django.db import models

# Create your models here.


# class Position(models.Model):
#    title = models.CharField(max_length=50)
#    def __str__(self):
#        return self.title


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    edad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    duracion = models.CharField(max_length=15)
    costo = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
