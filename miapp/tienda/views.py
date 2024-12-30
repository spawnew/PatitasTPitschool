from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def home1(request):
    diccionario={"nombre": "Juan", "edad": 20, "ciudad": "Madrid"}
    return render(request, 'home1.html', diccionario)
