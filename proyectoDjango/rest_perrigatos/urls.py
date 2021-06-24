from rest_perrigatos.views import lista_producto,manipular_producto
from django.urls import path, include



urlpatterns = [
    path('lista_producto',lista_producto, 'lista_producto'),
    path('datos_producto/<id>',manipular_producto,name="manipular_producto"),



]