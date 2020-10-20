from django import forms
from .models import Cita


class CitaForm(forms.ModelForm):

    class Meta:
        model = Cita
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(Cita, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False