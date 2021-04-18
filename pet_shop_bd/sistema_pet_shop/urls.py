from django.urls import path
from . import views

app_name = "sistema_pet_shop"

urlpatterns = [
    path('', views.Unidades.as_view(), name="home"),
    path('nova-unidade', views.novaUnidade, name="novaUnidade"),
    path('editar-unidade/<int:pk>', views.editUnidade, name="novaUnidade"),
    path('delete-unidade/<int:pk>', views.deleteUnidade, name='deleteUnidade')
]