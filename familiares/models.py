from django.db import models

# Create your models here.

class familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, default=True)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    dni =  models.CharField(max_length=40, unique=True)