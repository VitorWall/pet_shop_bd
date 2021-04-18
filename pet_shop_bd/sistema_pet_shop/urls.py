from django.urls import path
from . import views

app_name = "sistema_pet_shop"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('nova-unidade', views.novaUnidade, name="novaUnidade"),
]