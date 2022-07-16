from django.db import models

class Coche(models.Model):
    nombre = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    asientos = models.CharField(max_length=30)

class Añadir(models.Model):
    nombre= models.CharField(max_length=30)
    modelo= models.CharField(max_length=30)
    asientos= models.CharField(max_length=30)

class Inicio(models.Model):
    nombre=models.CharField(max_length=40)

def __str__(self):
      return self.name