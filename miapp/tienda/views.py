from pyexpat.errors import messages
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

from django.contrib import messages

from django.shortcuts import render
from .utils import get_random_dog

def home(request):
    return render(request, 'home.html')
@login_required
def contacto(request):
    
   
    return render(request, 'contacto.html')
@login_required
def buscarPerro(request):
    contexto={"Perro":Perro.objects.all()}
    return render(request, 'buscarPerro.html',contexto)

@login_required
def perroEncontrado(request):
    return render(request, 'perroEncontrado.html')
@login_required
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

class PerroList(LoginRequiredMixin,  ListView):
    model = Perro
    template_name = "perro_list.html"


class PerroCreate(LoginRequiredMixin, CreateView):
    model = Perro
    fields = ['nombre', 'edad','direccion','contacto','imagen']  
    template_name = 'perro_form.html'
    success_url = reverse_lazy('perro_list')
    
class  PerroUpdate(LoginRequiredMixin, UpdateView):
    model = Perro
    fields = ['nombre', 'edad', 'direccion','contacto','imagen']
    template_name = 'update_perro.html'
    success_url = reverse_lazy('perro_list')

class  PerroDelete(LoginRequiredMixin,  DeleteView):
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
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "registro.html", {"form": miForm })  
def salir( request):
    logout(request)
    messages.success(request ,"tu sesision se ha cerrado correctamente")
    return redirect ("home")

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "home.html")

    else:    
        form = AvatarForm()

    return render(request, "agregar_avatar.html", {"form": form })

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "miapp/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "miapp/editar_Perfil.html", {"form": form }) 


def random_dog_view(request):
  
    dog_image = get_random_dog()
    if not dog_image:
        return render(request, 'error.html', {'error': 'No se pudo obtener la imagen del perro.'})

    return render(request, 'random_dog.html', {'dog_image': dog_image})


