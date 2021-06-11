
from django.contrib import admin
from django.urls import path, include
from .views import home, seccionotros , contactanos, secciongatuna, Seccionperruna, inicioSesion, registro, carrito, cambiocontra, recuperacion,lista_regiones,guardar_usuario,guardar_comentario, listado,eliminar_listado,listar_tablas,modificar_pro,agregar_carr,eliminar_carro,guardar_producto,agregar_p,mostrar_p,carro1
urlpatterns = [
    path('', home, name="home"),
    path('mostrar_p/<int:id>', mostrar_p, name="mostrar_p"),
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
    #Ver si esta bien este
    path('guardar_comentario',guardar_comentario,name="guardar_comentario"),
    path('listado',listado,name="listado"),
    path('eliminar_listado/<int:id>',eliminar_listado,name="eliminar_listado"),
    path('listar_tablas/<int:id>',listar_tablas,name="listar_tablas"),
    path('modificar_pro',modificar_pro,name="modificar_pro"),
    
    path('agregar_carr',agregar_carr,name="agregar_carr"),
    path('eliminar_carro/<int:id>',eliminar_carro,name="eliminar_carro"),
    
    path('guardar_producto',guardar_producto,name="guardar_producto"),
    
    path('agregar_p',agregar_p,name="agregar_p"),
    path('carro1',carro1,name="carro1"),
    
    
]
