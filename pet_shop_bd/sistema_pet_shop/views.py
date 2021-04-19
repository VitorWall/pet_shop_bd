from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView, ListView
from .models import *
from .forms import *

# Create your views here.
class Unidades (ListView):
    model = Unidade

def novaUnidade (request):
    if request.method == 'POST':
        form = UnidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistema_pet_shop:unidades')
    form = UnidadeForm()

    return render(request,'nova_unidade.html',{'form': form})

def editUnidade (request, pk, template_name='sistema_pet_shop/edit_unidade.html'):
    unidade = get_object_or_404(Unidade, id=pk)
    form = UnidadeForm(request.POST or None, instance=unidade)
    if form.is_valid():
        form.save()
        return redirect('sistema_pet_shop:unidades')
    return render(request, template_name, {'form':form})

def deleteUnidade (request, pk, template_name=''):
    unidade = get_object_or_404(Unidade, id=pk)
    unidade.delete()
    return redirect('sistema_pet_shop:Uunidades')

class Clientes (ListView):
    model = Cliente

def novoCliente (request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistema_pet_shop:clientes')
    form = ClienteForm()

    return render(request,'novo_cliente.html',{'form': form})

def editCliente (request, pk, template_name='sistema_pet_shop/edit_cliente.html'):
    cliente = get_object_or_404(Cliente, id=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('sistema_pet_shop:clientes')
    return render(request, template_name, {'form':form})

def deleteCliente (request, pk, template_name=''):
    cliente = get_object_or_404(Cliente, id=pk)
    cliente.delete()
    return redirect('/clientes')
