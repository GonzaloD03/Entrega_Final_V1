from django import forms


class CocheFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    modelo= forms.CharField(max_length=30)
    asientos= forms.CharField(max_length=30)