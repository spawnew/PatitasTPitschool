from django.db import models
from django.db.models.fields.files import ImageField



class Perro(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    foto= models.ImageField(upload_to='perros', null=True, blank=True)
    email= models.EmailField()