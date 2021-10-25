from django.db.models import fields
from Controle.models import Oficio
from django import forms

class OficioForm (forms.ModelForm):
    class Meta:
        model = Oficio
        fields = ('numero_oficio')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields    #preciso buscar na sessão o endereço de quem fez login
        




