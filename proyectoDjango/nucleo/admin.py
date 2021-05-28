from django.contrib import admin
from .models import Categoria,Marca,Producto,Contacto,Usuario,Tipo_usuario,Region,Comuna,Direccion
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Comuna)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
admin.site.register(Region)
