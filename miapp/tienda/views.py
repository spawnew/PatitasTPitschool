from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login,logout
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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
    fields = ['nombre', 'edad','direccion','contacto']  
    template_name = 'perro_form.html'
    success_url = reverse_lazy('perro_list')
    
class  PerroUpdate(UpdateView):
    model = Perro
    fields = ['nombre', 'edad', 'direccion','contacto']
    template_name = 'update_perro.html'
    success_url = reverse_lazy('perro_list')

class  PerroDelete( DeleteView):
    model = Perro
    template_name = 'perro_confirm_delete.html'
    success_url = reverse_lazy('perro_list')




def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            
            return render(request, "home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "login.html", {"form": miForm })