from cmath import inf
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_recetas.models import *
from app_recetas.forms import Nueva_receta
from app_recetas.forms import Nuevo_ingrediente
from app_recetas.forms import New_mensaje
from app_recetas.forms import UserEditForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required




#INICIO

def inicio (request):
    return render(request, "app_recetas/index.html")

#RECETAS

def recetas (request):
    recetas = Receta.objects.all()
    datos = { "datos" : recetas}

    return render (request , "app_recetas/recetas.html" , datos)

#AGREGAR NUEVA RECETAS

@login_required
def nueva_receta(request):

    if request.method == 'POST':
        n_receta = Nueva_receta(request.POST)
        print(n_receta)

        if n_receta.is_valid:
            datos = n_receta.cleaned_data
            receta = Receta(nombre=datos['nombre'], ingrediente_uno=datos['ingrediente_uno'], ingrediente_dos=datos['ingrediente_dos'], ingrediente_tres=datos['ingrediente_tres'], tiempo=datos['tiempo'], descripcion=datos['descripcion'])
            receta.save()

            receta = Receta.objects.all() #cargo todos

            return render(request, "app_recetas/recetas.html" , {"datos": receta}) #renderizo nuevamente
    
    else:
        n_receta = Nueva_receta()
    
    return render(request, "app_recetas/nueva_receta.html",{"n_receta":n_receta})


#MODIFICAR RECETA
@login_required
def modificar_receta (request, nombre):
    receta = Receta.objects.get(nombre=nombre)

    if request.method == 'POST':
        n_receta = Nueva_receta(request.POST)
        print(n_receta)

        if n_receta.is_valid:
            datos = n_receta.cleaned_data

            receta.nombre = datos['nombre']
            receta.ingrediente_uno = datos['ingrediente_uno']
            receta.ingrediente_dos = datos['ingrediente_dos']
            receta.ingrediente_tres = datos['ingrediente_tres']
            receta.tiempo = datos['tiempo']
            receta.descripcion = datos['descripcion']
            
            receta.save()

            receta = Receta.objects.all() #cargo todos

            return render(request, "app_recetas/recetas.html" , {"datos": receta}) #renderizo nuevamente

    else:
        n_receta = Nueva_receta(initial={'nombre':receta.nombre , 'ingrediente_uno':receta.ingrediente_uno , 'ingrediente_dos':receta.ingrediente_dos , 'ingrediente_tres':receta.ingrediente_tres , 'tiempo':receta.tiempo , 'descripcion':receta.descripcion})

    return render(request, "app_recetas/modificar_receta.html", {"n_receta":n_receta , "receta":receta})


# BUSCAR RECETAS

def busqueda_receta(request):
    return render (request, "app_recetas/busqueda_receta.html")

def buscar_receta(request):
    if request.GET["ingrediente_uno"]:
        ingrediente_uno = request.GET['ingrediente_uno']
        recetas = Receta.objects.filter(ingrediente_uno__icontains=ingrediente_uno)
        
        return render (request , "app_recetas/resultado_recetas.html" , {"recetas":recetas , "ingrediente_uno":ingrediente_uno})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


#INGREDIENTES

def ingredientes (request):
    ingredientes = Ingrediente.objects.all()
    datos = { "datos" : ingredientes}
    return render(request, "app_recetas/ingredientes.html" , datos)

#AGREGAR NUEVO INGREDIENTE

@login_required
def nuevo_ingrediente(request):

    if request.method == 'POST':
        n_ingrediente = Nuevo_ingrediente(request.POST)
        print(n_ingrediente)

        if n_ingrediente.is_valid:
            datos = n_ingrediente.cleaned_data
            ingrediente = Ingrediente(nombre=datos['nombre'], tipo=datos['tipo'], conservacion=datos['conservacion'])
            ingrediente.save()

            ingrediente = Ingrediente.objects.all() #cargo todos

            return render(request, "app_recetas/ingredientes.html" , {"datos": ingrediente}) #renderizo nuevamente
    
    else:
        n_ingrediente = Nuevo_ingrediente()
    
    return render(request, "app_recetas/nuevo_ingrediente.html",{"n_ingrediente":n_ingrediente})

#MODIFICAR UN INGREDIENTE

@login_required
def modificar_ingrediente (request, nombre):
    ingrediente = Ingrediente.objects.get(nombre=nombre)

    if request.method == 'POST':
        n_ingrediente = Nuevo_ingrediente(request.POST)
        print(n_ingrediente)

        if n_ingrediente.is_valid:
            datos = n_ingrediente.cleaned_data

            ingrediente.nombre = datos['nombre'] #sobreescribo
            ingrediente.tipo = datos['tipo']
            ingrediente.conservacion = datos['conservacion']
            
            ingrediente.save()

            ingrediente = Ingrediente.objects.all() #cargo todos

            return render(request, "app_recetas/ingredientes.html" , {"datos": ingrediente}) #renderizo nuevamente

    else:
        n_ingrediente = Nuevo_ingrediente(initial={'nombre':ingrediente.nombre , 'tipo':ingrediente.tipo , 'conservacion':ingrediente.conservacion})

    return render(request, "app_recetas/modificar_ingrediente.html", {"n_ingrediente":n_ingrediente , "ingrediente":ingrediente})


#BORRAR INGREDIENTE

@login_required
def borrar_ingrediente(request, id_in):
    ingrediente = Ingrediente.objects.get(id=id_in) #lo encuentro
    ingrediente.delete() #lo borro

    ingrediente = Ingrediente.objects.all() #cargo todos

    return render(request, "app_recetas/ingredientes.html" , {"datos": ingrediente}) #renderizo nuevamente



#CONTACTO

def contacto (request):
    if request.method == 'POST':
        n_usuario = New_mensaje(request.POST)
        print(n_usuario)

        if n_usuario.is_valid:
            datos = n_usuario.cleaned_data
            usuario = Mensaje(usuario=datos['usuario'], email=datos['email'], mensaje=datos['mensaje'])
            usuario.save()
            return render(request, "app_recetas/index.html")
    
    else:
        n_usuario = New_mensaje()
    
    return render(request, "app_recetas/contacto.html",{"n_usuario":n_usuario})


#LOGIN
def login_request (request):

    if request.method == "POST":
        form = AuthenticationForm(request , data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            contra = form.cleaned_data.get('password')

            user = authenticate( username=usuario , email=email , password=contra)

            if user is not None:
                login(request,user)
                return render (request,"app_recetas/index.html")
            
            else:
                return render (request,"app_recetas/inicio.html" , {"mensaje":f"Los dos ingresados son incorrectos"})

        else:
            return render (request,"app_recetas/inicio.html" , {"mensaje":f"Los datos ingresados son incorrectos"})
            
    
    form = AuthenticationForm()
    return render (request , "app_recetas/login.html", {"form":form})


#REGISTER
def register (request):
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            
            form.save()
            return render (request,"app_recetas/nuevo_registro.html" , {"mensaje":f"¡Usuario creado con exito!"})

    else:
        form = UserRegisterForm()
    
    return render (request, "app_recetas/registro.html", {"form":form})


#EDITAR PERFIL
@login_required
def editar_perfil (request):

    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render (request , "app_recetas/index.html" , {"mensaje":f"Datos modificados con éxito!"} ) 



    else:
        formulario = UserEditForm(initial={'email':usuario.email})
        
    return render (request , "app_recetas/editar_perfil.html", {"formulario":formulario , "usuario":usuario} )

#ABOUT

def about(request):
    return render(request, "app_recetas/about.html")

