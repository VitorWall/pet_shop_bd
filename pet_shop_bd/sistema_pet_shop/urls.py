from django.urls import path
from . import views

app_name = "sistema_pet_shop"

urlpatterns = [
    path('', views.Unidades.as_view(), name="unidades"),
    path('detail-unidade/<int:pk>', views.DetailUnidade.as_view(), name="detail-unidade"),
    path('nova-unidade', views.novaUnidade, name="nova-unidade"),
    path('editar-unidade/<int:pk>', views.editUnidade, name="nova-unidade"),
    path('delete-unidade/<int:pk>', views.deleteUnidade, name='delete-unidade'),
    path('clientes', views.Clientes.as_view(), name="clientes"),
    path('detail-cliente/<int:pk>', views.DetailCliente.as_view(), name="detail-cliente"),
    path('novo-cliente', views.novoCliente, name="novo-cliente"),
    path('editar-cliente/<int:pk>', views.editCliente, name="novo-cliente"),
    path('delete-cliente/<int:pk>', views.deleteCliente, name='delete-cliente'),
    path('novo-pet/<int:pk>', views.novoPet, name="novo-pet"),
    path('editar-pet/<int:pk>', views.editPet, name="novo-pet"),
    path('delete-pet/<int:pk>', views.deletePet, name='delete-pet'),
]