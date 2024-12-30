from django.db import models




class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()