from django.db.models.query import InstanceCheckMeta
from django.http import request
from django.shortcuts import redirect, render, resolve_url
from .models import Carrito, Categoria, Marca, Pro_carrito, Region, Tipo_usuario, Usuario, Contacto,Producto,Venta,Detalle_venta
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    carrito = Carrito.objects.get(id_carrito = 4)
    template = {
        'verproducto' : verproducto,
        'carrito' : carrito
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





def registro(request):
    return render(request, 'nucleo/registro.html')


def carrito(request):
    car = Carrito.objects.get(id_carrito = 4)
    carro = Pro_carrito.objects.filter(carrito = car)
    total = Pro_carrito.objects.aggregate(sum1 = Sum('sub_total'))
    
    data = {
        'carro' : carro,
        'total' : total
    }
    return render(request, 'nucleo/carrito.html',data)




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
    
    user1 = User.objects.create_user(username = nom_usuario, email = correo_usuario, password = con_usuario)
    user1.first_name = nom_completo
    user1.last_name = nom_completo
    user1.is_staff = 1
    
    user1.save()
    Usuario.objects.create(nombre_completo=nom_completo,
                           alias=nom_usuario, email_u=correo_usuario, telofono_u=telefono, contraseña_u=con_usuario, run_u=run_usuario,
                           cod_post=codigo_postal, modo_osc=0, tipo_usuario=tipo_us, user = user1)
    
    
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





def agregar_carr(request):
    id_pro = request.POST['id_productop']
    id_pro1 = Producto.objects.get(id_producto = id_pro )
    id_carr = request.POST['carrito']
    id_carr2 = Carrito.objects.get(id_carrito = id_carr )
    canti = request.POST['cantidad']
    preci = request.POST['precio_p']
    sub_to = int(preci) * int(canti)

    Pro_carrito.objects.create(canti_pro =canti, sub_total = sub_to, producto = id_pro1, carrito = id_carr2)
    
    return redirect('carrito')



 



def eliminar_carro(request, id):
    carrito = Pro_carrito.objects.get(id_pro_carr = id)
    carrito.delete()
    messages.success(request,"Producto eliminado del carrito")
    return redirect('carrito')

#Duda profe.
def mod_cantidad(request, id):
    p = Pro_carrito.objects.get(id_pro_carr = id)
    #canti = request.POST['cantidad_p']
    canti = request.POST.get('cantidad_p')
    print(canti)
    p.canti_pro = canti
    p.save()

    return redirect('carrito')

def mod_cantidad2(request):
    p = Pro_carrito.objects.get(id_pro_carr = request.POST['codigo'])
    canti = request.POST['cantidad_p']
    subt = int(p.producto.precio) * int(canti)
    #canti = request.POST.get('cantidad_p')
   #print(canti)
    p.canti_pro = canti
    p.sub_total = subt
    p.save()

    return redirect('carrito')


def agregar_p(request):
    categoria = Categoria.objects.all()
    marca = Marca.objects.all()
    data = {
        'categorias' : categoria,
        'marcas' : marca
    }
    return render(request,'nucleo/agregar_p.html', data)

def guardar_producto(request):
    nom_producto = request.POST['nom_pro']
    st_pro = request.POST['pro_st']
    pre_pro = request.POST['precio_pro']
    valo_p = request.POST['valoracion_pro']
    sku_p = request.POST['sku_pro']
    des_p = request.POST['des_prod']
    col_pro = request.POST['color_prod']
    foto_p = request.FILES['foto_prod']
    cat1 = request.POST['categoria']
    cat2 = Categoria.objects.get(id_categoria=cat1)
    mar = request.POST['marca']
    mar2 = Marca.objects.get(id_marca=mar)

    Producto.objects.create(n_producto=nom_producto, stock=st_pro, precio=pre_pro, valoracion=valo_p,sku=sku_p, des_pro=des_p,color_pro=col_pro, foto_pro=foto_p,categoria = cat2, marca = mar2)
    
    messages.success(request, "Producto Agregado exitosamente")
    return redirect('listado')
    



def mostrar_p(request, id):
    producto = Producto.objects.get(id_producto = id)
    carrito = Carrito.objects.get(id_carrito = 4)
    template = {
        'verproducto' : producto,
        'carrito' : carrito
    }
    return render(request,'nucleo/Verproductop.html',template)

def carro1(request):
    carr1 = request.POST['carrito']
    carr2 = Carrito.objects.get(id_carrito = carr1)
    can = request.POST['cantidad']
    prec = request.POST['precio_p']
    id_pro = request.POST['id_productop']
    id_pro2 = Producto.objects.get(id_producto = id_pro)
    sub_to = int(prec) * int(can)

    carro = Pro_carrito.objects.create(canti_pro = can, sub_total = sub_to, producto = id_pro2, carrito = carr2 )
    
    return redirect('carrito')


def login_view(request):
    usuario = request.POST['username']
    contra = request.POST['password']
    user = authenticate(username = usuario, password = contra)

    if user is not None:
        if user.is_active:
            login(request,user)
            messages.success(request, 'SE HA INICIADO SESION CORRECTAMENTE')
        else:
            messages.error(request,'Usuario desabilitado')
    else:
        messages.error(request,'Usuario o Contraseña erronea')
    return redirect('inicioSesion')

def logout_view(request):
    logout(request)
    return redirect('home')

def inicioSesion(request):
    return render(request,'nucleo/inicioSesion.html')

def registro_django(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, 'Usuario creado')
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request , 'nucleo/registro2.html', context)


