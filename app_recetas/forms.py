from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Nueva_receta(forms.Form):
    nombre = forms.CharField()
    ingrediente_uno = forms.CharField()
    ingrediente_dos = forms.CharField()
    ingrediente_tres = forms.CharField()
    tiempo = forms.IntegerField()
    descripcion = forms.CharField()

class Nuevo_ingrediente(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()
    conservacion = forms.CharField()

class New_mensaje(forms.Form):
    usuario = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirmar contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1: forms.CharField(label="Contraseña" , widget=forms.PasswordInput )
    password1: forms.CharField(label="Repetir la c ontraseña" , widget=forms.PasswordInput )

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}





""" class New_recet(forms.Form):
    nombre = forms.CharField()
    ingredientes = forms.CharField()
    tiempo = forms.IntegerField()
    preparacion = forms.CharField()

class New_ingredient(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()
    propiedades = forms.CharField()
    conservacion = forms.CharField()

class Nuevo_usuario(forms.Form):
    nombre = forms.CharField()
    usuario = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()
 """
