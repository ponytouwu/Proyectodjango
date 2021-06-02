from django.db.models.query import InstanceCheckMeta
from django.shortcuts import redirect, render
from .models import Region, Tipo_usuario, Usuario, Contacto

# Create your views here.


def home(request):
    return render(request, 'nucleo/home.html')


def Verproductop(request):
    return render(request, 'nucleo/Verproductop.html')


def seccionotros(request):
    return render(request, 'nucleo/seccionotros.html')


def contactanos(request):
    return render(request, 'nucleo/contactanos.html')


def secciongatuna(request):
    return render(request, 'nucleo/secciongatuna.html')


def Seccionperruna(request):
    return render(request, 'nucleo/Seccionperruna.html')


def inicioSesion(request):
    return render(request, 'nucleo/inicioSesion.html')


def registro(request):
    return render(request, 'nucleo/registro.html')


def carrito(request):
    return render(request, 'nucleo/carrito.html')


def cambiocontra(request):
    return render(request, 'nucleo/cambiocontra.html')


def recuperacion(request):
    return render(request, 'nucleo/recuperacion.html')


def lista_regiones(request):
    regiones = Region.objects.all()  # obtengo los datos de la tabla
    # guardadndo en la variable entre "" los datos de regiones
    contexto = {"regiones": regiones}
    return render(request, 'nucleo/registro.html', contexto)


# el request es donde se guardan los datos de los formularios.
def guardar_usuario(request):
    nom_usuario = request.GET['usuario']
    con_usuario = request.GET['contraseña']
    nom_completo = request.GET['nombre']
    correo_usuario = request.GET['correo']
    region = request.GET['ciudad']
    region2 = Region.objects.get(id_region=region)
    direccion_us = request.GET['direccion']
    codigo_postal = request.GET['postal']
    telefono = request.GET['telefono']
    run_usuario = request.GET['rut']
    tipo_us = Tipo_usuario.objects.get(id_usu_tip=2)

    Usuario.objects.create(nombre_completo=nom_completo,
                           alias=nom_usuario, email_u=correo_usuario, telofono_u=telefono, contraseña_u=con_usuario, run_u=run_usuario,
                           cod_post=codigo_postal, modo_osc=0, tipo_usuario=tipo_us)

    return redirect('lista_regiones')

#como hay id iguales probar si no hace problemas con las del html registro
def guardar_comentario(request):  # guardado de comentario
    nombre_c = request.GET['nombre']
    snombre_c = request.GET['apellido']
    correo_con = request.GET['email']
    telefono_c = request.GET['telefono']
    comentario = request.GET['mensaje']
    # como no tenemos una tabla donde insertalos, supongo que con este siempre estara en 0=no leido 1=leido, se debe cambiar manualmente cuando se lea
    status_con = Contacto.objects.get(status_con=0)

    Usuario.objects.create(p_nombre =nombre_c, s_nombre=snombre_c,correo_con=correo_con,telefono=telefono_c,comentario=comentario,status_con=status_con)
    #no se a donde va el redirect, si tiene que ir a otra parte, pero retornara a la misma pagina
    return redirect('contactanos')