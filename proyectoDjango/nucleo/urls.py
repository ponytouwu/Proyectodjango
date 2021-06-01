
from django.contrib import admin
from django.urls import path, include
from .views import home, Verproductop, seccionotros , contactanos, secciongatuna, Seccionperruna, inicioSesion, registro, carrito, cambiocontra, recuperacion,lista_regiones,guardar_usuario
urlpatterns = [
    path('', home, name="home"),
    path('Verproductop', Verproductop, name="Verproductop"),
    path('seccionotros', seccionotros, name="seccionotros"),
    path('contactanos', contactanos, name="contactanos"),
    path('secciongatuna', secciongatuna, name="secciongatuna"), 
    path('Seccionperruna', Seccionperruna, name="Seccionperruna"),
    path('inicioSesion', inicioSesion, name="inicioSesion"),
    path('registro', registro, name="registro"),
    path('carrito',carrito,name="carrito"),
    path('cambiocontra',cambiocontra,name="cambiocontra"),
    path('recuperacion',recuperacion,name='recuperacion'),
    path('lista_regiones',lista_regiones,name="lista_regiones"),
    path('registro_usuario',guardar_usuario,name="registro_usuario"),
    
]
