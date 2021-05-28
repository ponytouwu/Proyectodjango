from django.shortcuts import render

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
    