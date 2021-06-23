from typing import Tuple
from django.db import models
from django.db.models.expressions import F
from django.contrib.auth.models import User
# Create your models here.



class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, verbose_name='id de la categoria')
    nom_cat = models.CharField(max_length=50,  blank=False, verbose_name='nombre de la categoria')

    def __str__(self):
        return self.nom_cat

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True, verbose_name='id de la marca')
    nom_mar = models.CharField(max_length=50, blank=False, verbose_name='nombre de la marca')

    def __str__(self):
        return self.nom_mar

#class Oferta(models.Model):
 #   id_oferta = models.AutoField(primary_key=True, verbose_name='id de la oferta')
  #  nom_oferta = models.CharField(max_length=100, null = True , verbose_name='nombre oferta')


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name='id del producto')
    n_producto = models.CharField(max_length=100, blank=False,verbose_name='nombre del producto')
    stock = models.IntegerField( blank=False,verbose_name='stock del producto')
    precio = models.IntegerField( blank=False,verbose_name='precio del producto')
    valoracion = models.IntegerField( blank=False,verbose_name='valoracion del producto')
    sku = models.IntegerField(blank=False, verbose_name='codigo sku del producto')
    des_pro = models.CharField(max_length=200,blank=False, verbose_name='descripcion del producto')
    color_pro = models.CharField(max_length=20,blank=False, verbose_name='color del producto')
    foto_pro = models.ImageField(upload_to = "producto")
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.n_producto

class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True, verbose_name='id del contacto')
    p_nombre = models.CharField(max_length=100, blank=False, verbose_name='primer nombre')
    s_nombre = models.CharField(max_length=100, blank=False, verbose_name='segundo nombre')
    correo_con = models.CharField(max_length=100, blank=False, verbose_name='correo del contacto')
    telefono = models.CharField(max_length=11, blank=False, verbose_name='telefono del contacto')
    comentario = models.CharField(max_length=200, blank=False, verbose_name='comentario del contacto')
    status_con = models.IntegerField(blank=False, verbose_name='status del comentario')
 
    def __str__(self): 
        return self.p_nombre 

class Tipo_usuario(models.Model):
    id_usu_tip = models.AutoField(primary_key=True, verbose_name='Id del usuario')
    nom_usu = models.CharField(max_length=50, blank=False, verbose_name='Tipo de usuario')
    
    def __str__(self):
        return self.nom_usu


#tabla usario hay que terminar de rellenar, ESTARIA LISTA


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True,verbose_name='id del contacto')
    nombre_completo = models.CharField(max_length=200, blank=False, verbose_name='nombre completo de la persona')
    alias = models.CharField(max_length=200, blank=False, verbose_name='nombre de usuario')
    email_u = models.CharField(max_length=100, blank=False, verbose_name='correo del usuario')
    telofono_u = models.CharField(max_length=11, blank=False, verbose_name='telefono del usuario')
    contraseña_u= models.CharField(max_length=20, blank=False, verbose_name='comentario del usuario')
    run_u = models.IntegerField(blank=False, verbose_name='run del usuario')
    cod_post = models.IntegerField(blank=False, verbose_name='codigo postal del usuario')
    modo_osc = models.IntegerField(blank=True, verbose_name='modo oscuro/modo normal')
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)
    user =  models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    def __str__(self): 
        return self.alias 

#NICO
class Region(models.Model):
    id_region = models.IntegerField(primary_key=True, verbose_name='Id de la region')
    nombre_region = models.CharField(max_length=100, blank=False, verbose_name='Nombre region')
    
    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True, verbose_name='Id de la comuna')
    nombre_comuna = models.CharField(max_length=100, blank=False, verbose_name='Nombre comuna')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comuna


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True, verbose_name='Id de la direccion')
    descrip_dir = models.CharField(max_length=100, blank=False, verbose_name='Descripcion de la direccion')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    #falta crear tabla usuario para unirla aqui como las foreanas, YA CREADA PARECE
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.descrip_dir





#AQUI TERMINA LO MIO (NICO), FALTARIA ORDENAR SOLAMENTE



class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True, verbose_name='id del carrito')
    f_comp = models.DateField(blank=False, verbose_name='Fecha de la compra')
    id_direccion_c = models.CharField(max_length=100,blank=True, verbose_name='direccion de la compra')
    status = models.IntegerField(blank=False, verbose_name='status del carrito')
    total_pre = models.IntegerField(blank=False, verbose_name='total del precio producto')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    
    


class Pro_carrito(models.Model):
    id_pro_carr = models.AutoField(primary_key=True, verbose_name='id del producto en el carrito')
    canti_pro = models.IntegerField(blank=False, verbose_name='cantidad de productos')
    sub_total = models.IntegerField(blank=False, verbose_name='sub total')
    producto = models.ForeignKey ( Producto , on_delete = models.CASCADE )
    carrito = models.ForeignKey(Carrito , on_delete = models.CASCADE)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True , verbose_name='Id de la venta')
    fecha_venta = models.DateField(blank=False , verbose_name="fecha de la venta")
    total_venta = models.IntegerField(blank=False, verbose_name='total de la venta')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 

class Detalle_venta(models.Model):
    id_detalle = models.AutoField(primary_key=True , verbose_name='Id del detalle de la venta')
    cantidad_sub = models.IntegerField(blank=False , verbose_name='cantidad subtotal')
    venta = models.ForeignKey(Venta, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
