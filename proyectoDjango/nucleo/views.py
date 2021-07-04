from django.http import request
from django.shortcuts import redirect, render
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
    carrito = Carrito.objects.all()
    usuarios = Usuario.objects.all()

    
    template1 = {
        'ofertas_loro' : ofertas_loro,
        'ofertas_perro' : ofertas_perro,
        'gatito_minino' : ofertas_gato,
        'paquete_huesos' : ofertas_hueso,
        'usuario' : usuarios,
        'carrito' : carrito

    }
    return render(request,'nucleo/home.html',template1)





def seccionotros(request):
    productos = Producto.objects.filter(categoria = 3)
    carrito = Carrito.objects.all()
    usuarios = Usuario.objects.all()
    data = {
        'productos' : productos,
        'usuario' : usuarios,
        'carrito' : carrito
        
    }
    return render(request, 'nucleo/seccionotros.html',data)


def contactanos(request):
    carrito = Carrito.objects.all()
    usuarios = Usuario.objects.all()
    data = {
        
        'usuario' : usuarios,
        'carrito' : carrito
        
    }
    return render(request, 'nucleo/contactanos.html',data)


def secciongatuna(request):
    productos = Producto.objects.filter(categoria = 2)
    carrito = Carrito.objects.all()
    usuarios = Usuario.objects.all()
    template = {
        'productos' : productos,
        'usuario' : usuarios,
        'carrito' : carrito
    }
    return render(request, 'nucleo/secciongatuna.html', template)


def Seccionperruna(request):
    productos = Producto.objects.filter(categoria = 1)
    carrito = Carrito.objects.all()
    usuarios = Usuario.objects.all()
    template = { #varaible de contexto
        'productos' : productos ,# Almacenamos en una "vartiable llamada productos (la que va en '') le asignamos el valor del productos (linea 38) "
        'usuario' : usuarios,
        'carrito' : carrito
    }
    return render(request, 'nucleo/Seccionperruna.html', template)





def registro(request):
    return render(request, 'nucleo/registro.html')

def mostrar_p(request, id):
    producto = Producto.objects.get(id_producto = id)
    carrito = Carrito.objects.all()
    usuarios = Usuario.objects.all()
    template = {
        'verproducto' : producto,
        'carrito' : carrito,
        'usuario' : usuarios
    }
    return render(request,'nucleo/Verproductop.html',template)

def carrito(request, id):
    car = Carrito.objects.get(id_carrito = id)
    carro = Pro_carrito.objects.filter(carrito = car)
    total = Pro_carrito.objects.filter(carrito = car).aggregate(sum1 = Sum('sub_total'))
    
    usuarios = Usuario.objects.all()
    carrito = Carrito.objects.all()
    prod = Pro_carrito.objects.all()
    

    data = {
        'carro' : carro,
        'total' : total,
        'usuario' : usuarios,
        'carrito' : carrito,
        'prod' : prod,
        'car' : car
        
    }
    return render(request, 'nucleo/carrito.html',data)




def carro1(request):
    
    
    carr1 = request.POST['carrito']
    carr2 = Carrito.objects.get(id_carrito = carr1)
    can = request.POST['cantidad']
    prec = request.POST['precio_p']
    id_pro = request.POST['id_productop']
    id_pro2 = Producto.objects.get(id_producto = id_pro)
    sub_to = int(prec) * int(can)

    carro = Pro_carrito.objects.create(canti_pro = can, sub_total = sub_to, producto = id_pro2, carrito = carr2 )
    
    return redirect('carrito' , id = carr1)



def eliminar_carro(request, id):
    carrito = Pro_carrito.objects.get(id_pro_carr = id)

    carrito.delete()
    
    return redirect('carrito', id = carrito.carrito.id_carrito)



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
    

    try:
        a = User.objects.get(username = nom_usuario)
        messages.error(request,'El nombre de usuario no esta disponible')
        return redirect('lista_regiones')
    except User.DoesNotExist:
        try:
            b = User.objects.get(email = correo_usuario)
            messages.error(request,'el correo no esta disponible')
            return redirect('lista_regiones')
        except User.DoesNotExist:
            user1 = User.objects.create_user(nom_usuario,correo_usuario,con_usuario)
            user1.first_name = nom_completo
            user1.last_name = nom_completo
            user1.is_staff = 1
    
            user1.save()

    
    
            usuario_c = Usuario.objects.create(nombre_completo=nom_completo,
                           alias=nom_usuario, email_u=correo_usuario, telofono_u=telefono, contraseña_u=con_usuario, run_u=run_usuario,
                           cod_post=codigo_postal, modo_osc=0, tipo_usuario=tipo_us, user = user1)
    
            Carrito.objects.create(f_comp = "2020-10-10" , id_direccion_c = 'un lugar cualquiera', status = 0, total_pre = 0, usuario = usuario_c )






   
            messages.success(request,"usuario guardado")
    
            return redirect('lista_regiones')



def listar_us(request):
    usuario = Usuario.objects.all()
    user_dj = User.objects.all()
    regiones = Region.objects.all()
    contexto = {
        'usuario' : usuario,
        'user_dj' : user_dj,
        "regiones": regiones
    }
    return render(request,'nucleo/listado_us.html',contexto)


def mod_usuario(request, id):
    usuario1 = Usuario.objects.get(id_usuario = id)
    
    tipo_us = Tipo_usuario.objects.all()
    contexto = {
        'usuario1' : usuario1,
        'tipo_us' : tipo_us
    }
    return render(request, 'nucleo/modificar_us.html',contexto)


def modificar_us(request):
    id_us = request.GET['id']
    no_us = request.GET['usuario_mod']
    contr = request.GET['contraseña_mod']
    nom_c = request.GET['nombre_mod']
    rut_m = request.GET['rut_mod']
    corr_m = request.GET['correo_mod']
    pos_mod = request.GET['postal_mod']
    tel_mod = request.GET['telefono_mod']
    tipo_us = request.GET['tipo_usuario']
    tipo_us2 = Tipo_usuario.objects.get(id_usu_tip = tipo_us )

    usuario_m = Usuario.objects.get(id_usuario = id_us)
    usuario_m.nombre_completo = nom_c
    usuario_m.alias = no_us
    usuario_m.email_u = corr_m
    usuario_m.telofono_u = tel_mod
    usuario_m.contraseña_u = contr
    usuario_m.run_u = rut_m
    usuario_m.cod_post = pos_mod
   
    usuario_m.tipo_usuario = tipo_us2
    usuario_m.save()
    
    usr_user = User.objects.get(username = no_us)
    
    if Usuario.objects.filter(tipo_usuario = 1):

        usr_user.is_superuser = True
        usr_user.first_name = nom_c
        usr_user.save()
        messages.success(request, 'El usuario a sido modificado')
        return redirect('listar_us')
        
    elif Usuario.objects.filter(tipo_usuario = 2):
        usr_user.is_superuser = False
        usr_user.first_name = nom_c
        usr_user.save()
        messages.success(request, 'El usuario a sido modificado')
        return redirect('home')
        

    
    

def eliminar_us(request, id):
    
    us = Usuario.objects.get(id_usuario = id)
    user = us.alias
   
    us1 = User.objects.get(username = user)
    us1.delete()
    us.delete()
    return redirect('listar_us')
    
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
    
        
    cat1 = request.POST['categoria']
    cat2 = Categoria.objects.get(id_categoria = cat1)
    mar = request.POST['marca']
    mar2 = Marca.objects.get(id_marca = mar )
    
    

    new_pro = Producto.objects.get(id_producto = id)

    if request.FILES.get('foto_pro') is not None:
        img_pro = request.POST['foto_pro']
        new_pro.foto_pro = img_pro

    new_pro.id_producto = id
    new_pro.n_producto = n_pro
    new_pro.stock = sto
    new_pro.precio = prec
    new_pro.valoracion = val
    new_pro.sku = sk
    new_pro.des_pro = des
    new_pro.color_pro = col
    new_pro.categoria = cat2
    new_pro.marca = mar2

    new_pro.save()

    messages.success(request,"Producto Modificado")

    return redirect('listado')







#Duda profe.
def mod_cantidad(request, id):
    p = Pro_carrito.objects.get(id_pro_carr = id)
    #canti = request.POST['cantidad_p']
    canti = request.POST.get('cantidad_p')
    print(canti)
    p.canti_pro = canti
    p.save()

    return redirect('carrito', id = p.carrito.id_carrito)

def mod_cantidad2(request):
    p = Pro_carrito.objects.get(id_pro_carr = request.POST['codigo'])
    canti = request.POST['cantidad_p']
    subt = int(p.producto.precio) * int(canti)
    #canti = request.POST.get('cantidad_p')
   #print(canti)
    p.canti_pro = canti
    p.sub_total = subt
    p.save()

    return redirect('carrito', id = p.carrito.id_carrito)


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
    








def login_view(request):
    usuario = request.POST['username']
    contra = request.POST['password']
    user = authenticate(username = usuario, password = contra)

    if user is not None:
        if user.is_active:
            login(request,user)
            messages.success(request,'Se a iniciado sesion correctamente')
            return redirect('home')
        else:
            messages.error(request,'Usuario desabilitado')
            return redirect('inicioSesion')
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


def mod_us_p(request):
    usuario = Usuario.objects.all()
    contexto = {
        'us' : usuario

    }
    return render(request, 'nucleo/modificar_us_p.html',contexto)


def actualziar_us(request):
    id_us = request.GET['id_mod']
    nom_usuario = request.GET['usuario_mod']
    con_usuario = request.GET['contra_mod']
    nom_completo = request.GET['nombre_mod']
    correo_usuario = request.GET['correo_mod']
    
    
    codigo_postal = request.GET['postal_mod']
    telefono = request.GET['telefono_mod']
    run_usuario = request.GET['rut_mod']
    tipo_us = Tipo_usuario.objects.get(id_usu_tip=2)
    
    


    new_usu = Usuario.objects.get(id_usuario = id_us)
    new_usu.nombre_completo = nom_completo
    new_usu.alias = nom_usuario
    new_usu.email_u = correo_usuario
    new_usu.telofono_u = telefono
    new_usu.contraseña_u = con_usuario
    new_usu.run_u = run_usuario
    new_usu.cod_post = codigo_postal
    new_usu.modo_osc = 0
    new_usu.tipo_usuario = tipo_us
    

    new_usu.save()

    return redirect('home')





def pago(request, id):
    car = Carrito.objects.get(id_carrito = id)
    us = Usuario.objects.all()
    carro = Pro_carrito.objects.filter(carrito = car)
    total = Pro_carrito.objects.filter(carrito = car).aggregate(sum1 = Sum('sub_total'))
    contexto = {
        'car' : car,
        'us' : us,
        'carro' : carro,
        'total' : total
    }

    return render(request, "nucleo/pago.html",contexto)


def compra_completa(request):
    id_carr = request.GET['id_carrito']
    id_carr2 = Carrito.objects.get(id_carrito = id_carr)
    id_us = request.GET['id_usuario']
    id_us2 = Usuario.objects.get(id_usuario = id_us)

    id_carr2.delete()

    Carrito.objects.create(f_comp = "2020-10-10" , id_direccion_c = 'un lugar cualquiera', status = 0, total_pre = 0, usuario = id_us2 )


    


    return redirect('home')