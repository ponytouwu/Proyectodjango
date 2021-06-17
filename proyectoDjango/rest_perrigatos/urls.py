from rest_perrigatos.views import lista_producto
from django.urls import path, include



urlpatterns = [
    path('lista_producto',lista_producto,'lista_producto')



]