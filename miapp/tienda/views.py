from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def contacto(request):
    
    return render(request, 'contacto.html')
def buscarPerro(request):
    return render(request, 'buscarPerro.html')


def perroEncontrado(request):
    return render(request, 'perroEncontrado.html')