from django import forms
from .models import Jugador

class FormulariJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nom', 'posicio', 'nacionalitat', 'titols']
