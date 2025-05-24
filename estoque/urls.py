from django.urls import path
from . import views

urlpatterns = [
    path("", views.ver_menu, name="ver_menu"),
    path("adicionar/", views.adicionar_produto, name="adicionar_produto"),
    path("menu/", views.ver_menu, name="ver_menu"),
    path("estoque",views.ver_estoque,name="ver_estoque"),
    path("clientes/",views.ver_clientes,name="ver_clientes"),
    path('deletar/<int:id>/', views.remover_produto, name='remover_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    
]
