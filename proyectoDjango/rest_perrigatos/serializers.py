
from django.db.models.base import Model

from rest_framework import serializers

from nucleo.models import Contacto, Producto


class ProductoSerializador(serializers.ModelSerializer):

    class Meta:

        model = Producto
        #datos que vamos a compartir con el rest 
        fields = ['id_producto','n_producto','stock','precio','valoracion','sku','des_pro','color_pro','foto_pro','categoria','marca']




class ContactoSerializador(serializers.ModelSerializer):

    class Meta:

        model = Contacto
        #datos que vamos a compartir con el rest 
        fields = ['id_contacto','p_nombre','s_nombre','correo_con','telefono','comentario','status_con']        