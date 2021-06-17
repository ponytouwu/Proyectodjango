
from django.db.models.base import Model

from rest_framework import serializers

from nucleo.models import Producto


class ProductoSerializador(serializers.ModelSerializer):

    class Meta:

        model = Producto
        #datos que vamos a compartir con el rest 
        fields = ['id_producto','n_producto','stock','precio','valoracion','sku','des_pro','color_pro','foto_pro','categoria','marca']