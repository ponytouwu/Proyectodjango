from django.shortcuts import redirect, render
from .models import Region,Usuario

# Create your views here.

def home(request):
    return render(request,'nucleo/home.html')

def Verproductop(request):
    return render(request,'nucleo/Verproductop.html')

def seccionotros(request):
    return render(request,'nucleo/seccionotros.html')

def contactanos(request):
    return render(request,'nucleo/contactanos.html')

def secciongatuna(request):
    return render(request,'nucleo/secciongatuna.html')

def Seccionperruna(request):
    return render(request,'nucleo/Seccionperruna.html')

def inicioSesion(request):
    return render(request,'nucleo/inicioSesion.html')

def registro(request):
    return render(request,'nucleo/registro.html')

def carrito(request):
    return render(request,'nucleo/carrito.html')

def cambiocontra(request):
    return render(request,'nucleo/cambiocontra.html')

def recuperacion(request):
    return render(request,'nucleo/recuperacion.html')

def lista_regiones(request):
    regiones = Region.objects.all() #obtengo los datos de la tabla
    contexto = {"regiones": regiones} #guardadndo en la variable entre "" los datos de regiones
    return render(request, 'nucleo/registro.html', contexto)

def guardar_usuario(request): # el request es donde se guardan los datos de los formularios.
    nom_usuario = request.GET['usuario']
    con_usuario = request.GET['contraseña']
    nom_completo = request.GET['nombre']
    correo_usuario = request.GET['correo']
    region = request.GET['ciudad']
    region2 = Region.objects.get(id_region = region)
    direccion_us = request.GET['direccion']
    codigo_postal = request.GET['postal']
    telefono = request.GET['telefono']
    run_usuario = request.GET['rut']

    Usuario.objects.create(nombre_completo = nom_completo , alias = nom_usuario, email_u = correo_usuario, telofono_u = telefono, contraseña_u = con_usuario, run_u = run_usuario, cod_post = codigo_postal , modo_osc = 0 ,codigo_postal = 1)
    
    return redirect('lista_regiones')

    