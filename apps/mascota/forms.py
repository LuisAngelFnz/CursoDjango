from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad',
            'fecha_rescate',
            'persona',
            'vacuna'
        ]

        labels = {
            'nombre'        : 'Nombre',
            'sexo'          : 'Sexo',
            'edad'          : 'Edad aproximada',
            'fecha_rescate' : 'Fecha de Rescate',
            'persona'       : 'Adoptante',
            'vacuna'        : 'vacunas'
        }

        widgets = {
            'nombre'        : forms.TextInput({'class':'form-group'}),
            'sexo'          : forms.TextInput({'class':'form-group'}),
            'edad'          : forms.TextInput({'class':'form-group'}),
            'fecha_rescate' : forms.TextInput({'class':'form-group'}),
            'persona'       : forms.Select({'class':'form-group'}),
            'vacuna'        : forms.CheckboxSelectMultiple({'class':'form-check'}),
        }
