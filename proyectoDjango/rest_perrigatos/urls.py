from django.urls import path
from .views import lista_contacto, lista_producto1, manipular_contacto,manipular_producto1
from .viewslogin import login   



urlpatterns = [
    path('nueva_lista_producto',lista_producto1, name='nueva_lista_producto'),
    path('nuevos_datos_producto/<id>',manipular_producto1,name="manipular_producto"),
    path('loginRest',login,name="loginRest"),
    path('lista_contacto',lista_contacto,name="lista_contacto"),
    path('manipular_contacto/<id>',manipular_contacto,name="manipular_contacto"),


]