from django import forms
from .models import Red


class RedForm(forms.ModelForm):

    class Meta:
        model = Red
        fields = ('nombre', 'descripcion', 'tipo', 'ip', 'mascara', 'puerta_enlace', 'estado', 'latitud', 'longitud', 'dispositivos')
        
    def __init__(self, *args, **kwargs):
        super(RedForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo'].widget.attrs.update({'class': 'form-control'})
        self.fields['ip'].widget.attrs.update({'class': 'form-control'})
        self.fields['mascara'].widget.attrs.update({'class': 'form-control'})
        self.fields['puerta_enlace'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        self.fields['latitud'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitud'].widget.attrs.update({'class': 'form-control'})
        self.fields['dispositivos'].widget.attrs.update({'class': 'form-control'})
