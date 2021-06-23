
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import home, inicioSesion, seccionotros , contactanos, mod_cantidad2,secciongatuna, Seccionperruna, registro, carrito, cambiocontra, recuperacion,lista_regiones,guardar_usuario,guardar_comentario, listado,eliminar_listado,listar_tablas,modificar_pro,agregar_carr,eliminar_carro,guardar_producto,agregar_p,mostrar_p,carro1,login_view,logout_view,registro_django,mod_cantidad
urlpatterns = [
    path('', home, name="home"),
    path('mostrar_p/<int:id>', mostrar_p, name="mostrar_p"),
    path('seccionotros', seccionotros, name="seccionotros"),
    path('contactanos', login_required(contactanos), name="contactanos"),
    path('secciongatuna', secciongatuna, name="secciongatuna"), 
    path('Seccionperruna', Seccionperruna, name="Seccionperruna"),
    path('accounts/login/', LoginView.as_view(template_name = 'nucleo/inicioSesion.html'), name="inicioSesion"),
    #path('CerrarSesion/', LogoutView.as_view(template_name = 'nucleo/home.html'),name='CerrarSesion'),
    path('sesion/',login_view,name='sesion'),
    path('inicioSesion',inicioSesion,name='inicioSesion'),
    path('CerrarSesion/',logout_view, name='CerrarSesion'),
    path('registro', registro, name="registro"),
    path('carrito',login_required(carrito),name="carrito"),
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
    path('registro2/',registro_django, name ="registro2" ),
    
    path('mod_cantidad/<int:id>',mod_cantidad, name ="mod_cantidad" ),

    path('mod_cantidad2',mod_cantidad2, name ="mod_cantidad2" ),
    
    
    
]
