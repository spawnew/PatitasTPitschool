from django.db import models
from django.db.models.fields.files import ImageField



from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
   