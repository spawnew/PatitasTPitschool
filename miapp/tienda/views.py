from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


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
            fotoNombre = miForm.cleaned_data["foto"]
            perro = Perro(nombre=perroNombre, edad=edadNombre, foto=fotoNombre)
            perro.save()
           
            mensaje = "¡Perro registrado con éxito!"
            return render(request, "buscarPerro.html", {"mensaje": mensaje})
    else:
        miForm = BuscarPerroForm()  

    return render(request, "buscarPerroForm.html", {"form": miForm})

class PerroList( ListView):
    model = Perro
    template_name = "perro_list.html"


class PerroCreate(CreateView):
    model = Perro
    fields = ['nombre', 'edad']  
    template_name = 'perro_form.html'
    success_url = reverse_lazy('perro_list')
    
class  PerroUpdate(UpdateView):
    model = Perro
    fields = ['nombre', 'edad', ]
    success_url = reverse_lazy('perro_list')

class  PerroDelete( DeleteView):
    model = Perro
    template_name = 'perro_confirm_delete.html'
    success_url = reverse_lazy('perro_list')
