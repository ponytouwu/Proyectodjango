
from django.shortcuts import render

from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.models import Token

from django.contrib.auth.hashers import check_password  

from django.contrib.auth.models import User

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    u = data['username']
    c = data['password']

    try:
        user = User.objects.get(username = u)
    except User.DoesNotExist:
        return Response("Usuario Incorrecto")

    contra_valida = check_password(c,user.password)
    if not contra_valida:
        return Response("Contraseña Incorrecta")

    #permite conocer o crear el token
    token,created = Token.objects.get_or_create(user = user)
    return Response(token.key)