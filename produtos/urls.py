from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrada/<int:id>/', views.entrada_estoque, name='entrada'),
    path('saida/<int:id>/', views.saida_estoque, name='saida'),
    path('vendas/nova/', views.criar_venda, name='criar_venda'),
]
