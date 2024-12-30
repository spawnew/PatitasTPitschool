

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
      path('home', views.home, name="home"),
        path('home1', views.home1, name="home1"),

]
