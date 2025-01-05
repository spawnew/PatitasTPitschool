from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User


from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=40)
    contacto=models.EmailField(("@gmail"), max_length=254)
    
    class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 
    
    