from django.shortcuts import render
from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')
def contacto(request):
    
    return render(request, 'contacto.html')
def buscarPerro(request):
    contexto={"Perro":Perro.objects.all()}
    return render(request, 'buscarPerro.html',contexto)


def perroEncontrado(request):
    return render(request, 'perroEncontrado.html')

def buscarPerroForm(request):
    if request.method == "POST":
        miForm = BuscarPerroForm(request.POST, request.FILES)  # Instancia del formulario con datos
        if miForm.is_valid():
            
            perroNombre = miForm.cleaned_data['nombre']
            edadNombre = miForm.cleaned_data["edad"]
            perro = Perro(nombre=perroNombre, edad=edadNombre)
            perro.save()
           
            mensaje = "¡Perro registrado con éxito!"
            return render(request, "buscarPerro.html", {"mensaje": mensaje})
    else:
        miForm = BuscarPerroForm()  # Instancia del formulario vacío

    return render(request, "buscarPerroForm.html", {"form": miForm})

