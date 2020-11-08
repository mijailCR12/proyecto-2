from django import forms
from django.forms.widgets import Widget
from .models import Cita, Cliente, Empleado, Servicio


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('Nombre', 'Telefono', 'Correo',
                  'Ubicacion')
        labels = {
            'nombre': 'nombre',
            'telefono': 'telefono'
        }


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ('Nombre', 'Telefono', 'Correo',
                  'Especialidad', 'Ubicacion', 'Edad')
        labels = {
            'nombre': 'nombre',
            'telefono': 'telefono'
        }


class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ('Nombre', 'Descripcion', 'Duracion',
                  'Costo')
        labels = {
            'nombre': 'nombre',
            'descripcion': 'descripcion'
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class CitaForm(forms.ModelForm):

    class Meta:
        model = Cita
        fields = ('detalle', 'fecha', 'idCliente',
                  'idServicio', 'idEmpleado')
        labels = {
            'idCliente': 'detalle',
        }
        widgets = {'fecha': DateInput}

    idCliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    idServicio = forms.ModelChoiceField(queryset=Servicio.objects.all())
    idEmpleado = forms.ModelChoiceField(queryset=Empleado.objects.all())
