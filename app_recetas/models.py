import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length=40)
    ingrediente_uno = models.CharField(max_length=250)
    ingrediente_dos = models.CharField(max_length=250)
    ingrediente_tres = models.CharField(max_length=250)
    tiempo = models.IntegerField()
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f"Nombre:{self.nombre}"

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    conservacion = models.CharField(max_length=250)

    def __str__(self):
        return f"Nombre:{self.nombre}"

class Mensaje(models.Model):
    usuario = models.CharField(max_length=8)
    email = models.EmailField()
    mensaje = models.CharField(max_length=250)

    def __str__(self):
        return f"Usuario:{self.usuario}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True)
