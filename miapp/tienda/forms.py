




from django import forms 


class BuscarPerroForm(forms.Form):
    nombre=forms.CharField(max_length=40)                         
    edad=forms.IntegerField()
