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
    path('funcionarios/<int:pk>', views.Funcionarios.as_view(), name="funcionarios"),
    path('novo-servico', views.novoServico, name="novo-servico"),
    path('servicos', views.Servicos.as_view(), name="servicos"),
    path('editar-servico/<int:pk>', views.editServico, name="novo-servico"),
    path('delete-servico/<int:pk>', views.deleteServico, name='delete-servico'),
    path('nova-acomodacao', views.novaAcomodacao, name="nova-acomodacao"),
    path('acomodacoes', views.Acomodacoes.as_view(), name="acomodacoes"),
    path('editar-acomodacao/<int:pk>', views.editAcomodacao, name="nova-acomodacao"),
    path('delete-acomodacao/<int:pk>', views.deleteAcomodacao, name='delete-acomodacao'),
    
]   