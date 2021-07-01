from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers
from nucleo.models import Producto
from rest_perrigatos.serializers import ProductoSerializador
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
# metodo que vimos con el profe para modificar y enviar a traves de la aplicacion, instalar extension advanced REST client
# luego copiar url numeros/api/lista_producto ver si anda y luego copiar la url en el advance
def lista_producto1(request):

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


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def manipular_producto1(request, id):

    try:

        p = Producto.objects.get(id_producto=id)

    except Producto.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ProductoSerializador(p)

        return Response(serializer.data)

    elif request.method == 'PUT':

        data2 = JSONParser().parse(request)

        serializer = ProductoSerializador(p, data=data2)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        p.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
