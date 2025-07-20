from django.urls import path
from . import views

app_name = 'clientes'  # Adiciona namespace para evitar conflitos

urlpatterns = [
    path('', views.lista_clientes, name='lista'),
    path('novo/', views.cria_cliente, name='criar'),
    path('editar/<int:pk>/', views.atualiza_cliente, name='editar'),
    path('deletar/<int:pk>/', views.deleta_cliente, name='deletar'),
    path('buscar/', views.busca_cliente, name='buscar'),
]

urlpatterns += [
    path('leia-mais/', views.leia_mais, name='leia_mais'),
]