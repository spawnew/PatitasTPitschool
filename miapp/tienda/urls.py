
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('home', views.home, name="home"),
    path('contacto', views.contacto, name="contacto"),
    path('perro_list', views.PerroList.as_view(), name="perro_list"),
    path('perroEncontrado', views.perroEncontrado, name="perroEncontrado"),
    path('buscarPerroForm', views.buscarPerroForm, name="buscarPerroForm"),
    path('create_perro', views.PerroCreate.as_view(), name="create_perro"),
   
]

