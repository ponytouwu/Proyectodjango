from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='id de la categoria')
    nom_cat = models.CharField(max_length=50,  blank=False, verbose_name='nombre de la categoria')

    def __str__(self):
        return self.nom_cat

class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True, verbose_name='id de la marca')
    nom_mar = models.CharField(max_length=50, blank=False, verbose_name='nombre de la marca')

    def __str__(self):
        return self.nom_mar

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name='id del producto')
    n_producto = models.CharField(max_length=100, blank=False,verbose_name='nombre del producto')
    stock = models.IntegerField( blank=False,verbose_name='stock del producto')
    precio = models.IntegerField( blank=False,verbose_name='precio del producto')
    valoracion = models.IntegerField( blank=False,verbose_name='valoracion del producto')
    sku = models.IntegerField(blank=False, verbose_name='codigo sku del producto')
    des_pro = models.CharField(max_length=200,blank=False, verbose_name='descripcion del producto')
    color_pro = models.CharField(max_length=20,blank=False, verbose_name='color del producto')
    foto_pro = models.CharField(max_length=20,blank=False, verbose_name='foto del producto')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.n_producto

class Contacto(models.Model):
    id_contacto = models.IntegerField(primary_key=True, verbose_name='id del contacto')
    p_nombre = models.CharField(max_length=100, blank=False, verbose_name='primer nombre')
    s_nombre = models.CharField(max_length=100, blank=False, verbose_name='segundo nombre')
    correo_con = models.CharField(max_length=100, blank=False, verbose_name='correo del contacto')
    telefono = models.CharField(max_length=11, blank=False, verbose_name='telefono del contacto')
    comentario = models.CharField(max_length=200, blank=False, verbose_name='comentario del contacto')
    status_con = models.IntegerField(blank=False, verbose_name='status del comentario')
 
    def __str__(self): 
        return self.p_nombre 

#NICO
class Region(models.model):
    id_region = models.IntegerField(primary_key=True, verbose_name='Id de la region')
    nombre_region = models.CharField(max_length=100, blank=False, verbose_name='Nombre region')
    
    def __str__(self):
        return self.nombre_region

class Comuna(models.model):
    id_comuna = models.IntegerField(primary_key=True, verbose_name='Id de la comuna')
    nombre_comuna = models.CharField(max_length=100, blank=False, verbose_name='Nombre comuna')
    region = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comuna


class Direccion(models.model):
    id_direccion = models.IntegerField(primary_key=True, verbose_name='Id de la direccion')
    descrip_dir = models.CharField(max_length=100, blank=False, verbose_name='Descripcion de la direccion')
    comuna = models.ForeignKey(Marca, on_delete=models.CASCADE)
    #falta crear tabla usuario para unirla aqui como las foreanas, YA CREADA PARECE
    Usuario = models.ForeignKey(Marca, on_delete=models.CASCADE)
    def __str__(self):
        return self.descrip_dir



class Tipo_usuario(models.model):
    id_usu_tip = models.IntegerField(primary_key=True, verbose_name='Id del usuario')
    nom_usu = models.CharField(max_length=50, blank=False, verbose_name='Tipo de usuario')
    
    def __str__(self):
        return self.nom_usu


#tabla usario hay que terminar de rellenar, ESTARIA LISTA


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name='id del contacto')
    nombre_u = models.CharField(max_length=100, blank=False, verbose_name='nombre usuario')
    apellido_u = models.CharField(max_length=100, blank=False, verbose_name='apellido usuario')
    email_u = models.CharField(max_length=100, blank=False, verbose_name='correo del usuario')
    telofono_u = models.CharField(max_length=11, blank=False, verbose_name='telefono del usuario')
    contraseña_u= models.CharField(max_length=20, blank=False, verbose_name='comentario del usuario')
    run_u = models.IntegerField(blank=False, verbose_name='run del usuario')
    dv_run = models.CharField(max_length=1, blank=False, verbose_name='digito verificador del usuario')
    cod_post = models.IntegerField(blank=False, verbose_name='codigo postal del usuario')
    modo_osc = models.IntegerField(blank=False, verbose_name='modo oscuro/modo normal')
    tipo_usuario = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.run_u 

#AQUI TERMINA LO MIO (NICO), FALTARIA ORDENAR SOLAMENTE