from django.urls import path
from . import views

app_name = "sistema_pet_shop"

urlpatterns = [
    path('', views.Unidades.as_view(), name="unidades"),
    path('clientes', views.Clientes.as_view(), name="clientes"),
    path('nova-unidade', views.novaUnidade, name="novaUnidade"),
    path('editar-unidade/<int:pk>', views.editUnidade, name="novaUnidade"),
    path('delete-unidade/<int:pk>', views.deleteUnidade, name='deleteUnidade'),
    path('novo-cliente', views.novoCliente, name="novaCliente"),
    path('editar-cliente/<int:pk>', views.editCliente, name="novaCliente"),
    path('delete-cliente/<int:pk>', views.deleteCliente, name='deleteCliente')
]