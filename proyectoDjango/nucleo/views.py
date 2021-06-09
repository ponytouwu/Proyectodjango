from django.db.models.query import InstanceCheckMeta
from django.shortcuts import redirect, render
from .models import Categoria, Marca, Region, Tipo_usuario, Usuario, Contacto,Producto
from django.contrib import messages
# Create your views here.


def home(request):
    ofertas_loro = Producto.objects.get(n_producto = "Comida para Loros")
    ofertas_perro = Producto.objects.get(n_producto = "Cama para tu mascota")
    ofertas_gato = Producto.objects.get(n_producto = "Comida para gatos y perros")
    ofertas_hueso = Producto.objects.get(n_producto = "Huesitos 4 por paquete")
    template = {
        'ofertas_loro' : ofertas_loro,
        'ofertas_perro' : ofertas_perro,
        'gatito_minino' : ofertas_gato,
        'paquete_huesos' : ofertas_hueso

    }
    return render(request, 'nucleo/home.html',template)


def Verproductop(request):
    verproducto = Producto.objects.get(n_producto = "cepillo para perros peludos")
    template = {
        'verproducto' : verproducto
    }
    return render(request, 'nucleo/Verproductop.html',template )


def seccionotros(request):
    productos = Producto.objects.filter(categoria = 3)
    data = {
        'productos' : productos
        
    }
    return render(request, 'nucleo/seccionotros.html',data)


def contactanos(request):
    return render(request, 'nucleo/contactanos.html')


def secciongatuna(request):
    productos = Producto.objects.filter(categoria = 2)
    template = {
        'productos' : productos
    }
    return render(request, 'nucleo/secciongatuna.html', template)


def Seccionperruna(request):
    productos = Producto.objects.filter(categoria = 1)
    template = { #varaible de contexto
        'productos' : productos # Almacenamos en una "vartiable llamada productos (la que va en '') le asignamos el valor del productos (linea 38) "
    }
    return render(request, 'nucleo/Seccionperruna.html', template)


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
    messages.success(request,"usuario guardado")
    return redirect('lista_regiones')

#como hay id iguales probar si no hace problemas con las del html registro
def guardar_comentario(request):  # guardado de comentario
    nombre_c = request.GET['nombre']
    snombre_c = request.GET['apellido']
    correo_c = request.GET['email']
    telefono_c = request.GET['telefono']
    comentario_c = request.GET['mensaje']
    # como no tenemos una tabla donde insertalos, supongo que con este siempre estara en 0=no leido 1=leido, se debe cambiar manualmente cuando se lea
    status_com = 0

    Contacto.objects.create(p_nombre = nombre_c, s_nombre = snombre_c, correo_con = correo_c, telefono = telefono_c, comentario = comentario_c, status_con = status_com )
    #no se a donde va el redirect, si tiene que ir a otra parte, pero retornara a la misma pagina
    messages.success(request,"Mensaje enviado")
    return render(request, 'nucleo/contactanos.html')

def listado(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'nucleo/listado.html', data)

def eliminar_listado(request, id):
    
    producto = Producto.objects.get(id_producto = id)
    producto.delete()
    messages.success(request,"Producto Eliminado")

    return redirect('listado')

def listar_tablas(request, id):
    producto = Producto.objects.get(id_producto = id)
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()  # obtengo los datos de la tabla
    # guardadndo en la variable entre "" los datos de regiones
    contexto = {
        "producto" : producto,
        "categorias": categorias,
        "marcas" : marcas
        }
    return render(request, 'nucleo/modificar_p.html', contexto)
   
def modificar_pro(request):
    id = request.POST['id_producto']
    n_pro = request.POST['nombre']
    sto = request.POST['stock']
    prec = request.POST['precio']
    val = request.POST['valoracion']
    sk = request.POST['sku']
    des = request.POST['des_pro']
    col = request.POST['color_pro']
    fot = request.FILES['foto_pro']
    cat1 = request.POST['categoria']
    cat2 = Categoria.objects.get(id_categoria = cat1)
    mar = request.POST['marca']
    mar2 = Marca.objects.get(id_marca = mar )
    
    

    new_pro = Producto.objects.get(id_producto = id)
    new_pro.id_producto = id
    new_pro.n_producto = n_pro
    new_pro.stock = sto
    new_pro.precio = prec
    new_pro.valoracion = val
    new_pro.sku = sk
    new_pro.des_pro = des
    new_pro.color_pro = col
    new_pro.foto_pro = fot
    new_pro.categoria = cat2
    new_pro.marca = mar2

    new_pro.save()

    messages.success(request,"Producto Modificado")

    return redirect('listado')






