from django.urls import path
from .views import lista_producto1,manipular_producto1
from .viewslogin import login   



urlpatterns = [
    path('nueva_lista_producto',lista_producto1, name='nueva_lista_producto'),
    path('nuevos_datos_producto/<id>',manipular_producto1,name="manipular_producto"),
    path('loginRest',login,name="loginRest"),


]