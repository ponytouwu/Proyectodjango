
from django.contrib import admin
from django.urls import path, include
from .views import home, Verproductop, seccionotros , contactanos, secciongatuna, Seccionperruna, inicioSesion, registro, carrito, cambiocontra, recuperacion,lista_regiones,guardar_usuario,guardar_comentario, listado,eliminar_listado,listar_tablas,modificar_pro,huesitos,body,shampo,agregar_carr,eliminar_carro,rascador,guardar_producto,agregar_p,camarote,baño_g,comida_g,cama_p,acuario,dispensador,comida_a,comida_peces,loro
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
    #Ver si esta bien este
    path('guardar_comentario',guardar_comentario,name="guardar_comentario"),
    path('listado',listado,name="listado"),
    path('eliminar_listado/<int:id>',eliminar_listado,name="eliminar_listado"),
    path('listar_tablas/<int:id>',listar_tablas,name="listar_tablas"),
    path('modificar_pro',modificar_pro,name="modificar_pro"),
    path('huesitos',huesitos,name="huesitos"),
    path('body',body,name="body"),
    path('shampo',shampo,name="shampo"),
    path('agregar_carr',agregar_carr,name="agregar_carr"),
    path('eliminar_carro/<int:id>',eliminar_carro,name="eliminar_carro"),
    path('rascador',rascador,name="rascador"),
    path('guardar_producto',guardar_producto,name="guardar_producto"),
    
    path('agregar_p',agregar_p,name="agregar_p"),
    path('camarote',camarote,name="camarote"),
    path('baño_g',baño_g,name="baño_g"),
    path('comida_g',comida_g,name="comida_g"),
    path('cama_p',cama_p,name="cama_p"),
    path('acuario',acuario,name="acuario"),
    path('dispensador',dispensador,name="dispensador"),
    path('comida_a',comida_a,name="comida_a"),
    path('comida_peces',comida_peces,name="comida_peces"),
    path('loro',loro,name="loro"),

    
]
