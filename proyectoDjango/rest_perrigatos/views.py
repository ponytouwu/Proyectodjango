
from rest_perrigatos.serializers import ProductoSerializador
from nucleo.models import Producto
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers

# Create your views here.


@csrf_exempt
@api_view(['GET', 'POST'])
#metodo que vimos con el profe para modificar y enviar a traves de la aplicacion, instalar extension advanced REST client
#luego copiar url numeros/api/lista_producto ver si anda y luego copiar la url en el advance
def lista_producto(request):

    if request.method == 'GET':

        p = Producto.objects.all()

        serializer = ProductoSerializador(p, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        data2 = JSONParser().parse(request)

        serializer = ProductoSerializador(data=data2)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
