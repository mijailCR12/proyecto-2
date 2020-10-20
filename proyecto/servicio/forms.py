from django import forms
from .models import Servicio


class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ('nombre', 'descripcion', 'duracion', 'costo')
        labels = {
            'nombre': 'Nombre',
            'costo': 'Precio'
        }
