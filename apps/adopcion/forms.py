from django import forms

from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):

    class Meta:

        model = Persona

        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio'
        ]

        label = {
            'nombre'    : 'Nombre',
            'apellidos' : 'Apellidos',
            'edad'      : 'Edad',
            'telefono'  : 'Telefono',
            'email'     : 'Correo Electrónico',
            'domicilio' : 'Domicilio'
        }

        widgets = {
            'nombre'    : forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
            'edad'      : forms.TextInput(attrs={'class':'form-control'}),
            'telefono'  : forms.TextInput(attrs={'class':'form-control'}),
            'email'     : forms.TextInput(attrs={'class':'form-control'}),
            'domicilio' : forms.Textarea(attrs={'class':'form-control'}),
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        
        fields = ['numero_mascotas','razones']
        
        labels = {
            'numero_mascotas':'Número de Mascotas',
            'razones':'Razones de adopción'
        }

        widgets = {
            'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
            'razones':forms.Textarea(attrs={'class':'form-control'})
        }