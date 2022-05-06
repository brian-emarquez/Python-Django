from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label= "Nonbre", required=True)
    email = forms.CharField(label= "Email", required=True)
    contenido = forms.CharField(label= "Contenido")

