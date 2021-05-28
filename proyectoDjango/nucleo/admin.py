from django.contrib import admin
from .models import Categoria,Marca,Producto,Contacto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)
