from django.urls import path
from . import views

urlpatterns = [
    path("", views.loja_python, name="loja_python"),
    path("adicionar/", views.adicionar_produto, name="adicionar_produto"),
    path("menu/", views.ver_menu, name="ver_menu"),
    path("estoque", views.ver_estoque, name="ver_estoque"),
    path("estoque_falta", views.ver_estoque_falta, name="estoque_falta"),
    path("clientes/", views.ver_clientes, name="ver_clientes"),
    path("deletar/<int:id>/", views.remover_produto, name="remover_produto"),
    path("editar/<int:id>/", views.editar_produto, name="editar_produto"),
    path("novocliente/", views.adicionar_cliente, name="adicionar_cliente"),
    path("editarcliente/<int:id>/", views.editar_cliente, name="editar_cliente"),
    path("removercliente/<int:id>/", views.remover_cliente, name="remover_cliente"),
]
