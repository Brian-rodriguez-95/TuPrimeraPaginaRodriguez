
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("clientes/", views.lista_clientes, name="lista_clientes"),
    path("clientes/nuevo/", views.agregar_cliente, name="agregar_cliente"),
]
