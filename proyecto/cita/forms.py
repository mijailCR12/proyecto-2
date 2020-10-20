from django import forms
from .models import Cliente, Empleado, Servicio


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre', 'telefono', 'correo',
                  'ubicacion')
        labels = {
            'nombre': 'nombre',
            'telefono': 'telefono'
        }


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ('nombre', 'telefono', 'correo',
                  'especialidad', 'ubicacion', 'edad')
        labels = {
            'nombre': 'nombre',
            'telefono': 'telefono'
        }


class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ('nombre', 'descripcion', 'duracion',
                  'costo')
        labels = {
            'nombre': 'nombre',
            'descripcion': 'descripcion'
        }
