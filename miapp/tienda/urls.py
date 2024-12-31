
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('home', views.home, name="home"),
    path('contacto', views.contacto, name="contacto"),
    path('buscarPerro', views.buscarPerro, name="buscarPerro"),
    path('perroEncontrado', views.perroEncontrado, name="perroEncontrado"),
    path('buscarPerroForm', views.buscarPerroForm, name="buscarPerroForm"),
]