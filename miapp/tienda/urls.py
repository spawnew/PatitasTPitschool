
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
    
    path('update_perro/<int:pk>/', views.PerroUpdate.as_view(), name="update_perro" ),
    path('delete_perro/<int:pk>/', views.PerroDelete.as_view(), name="delete_perro" ), 
   
    path('agregar_avatar/', views.agregar_avatar, name="agregar_avatar"),
   path('editar_perfil/', views.editarPerfil, name="editar_perfil"),
   
   path ('salir/' , views.salir , name="salir"),
    path('login/', views.login_request, name="login"),
     path('registro/', views.register, name="registro"),



    path('random-dog/', views.random_dog_view, name='random_dog'),
  
  
  

   
   
   
   
   
   
]

