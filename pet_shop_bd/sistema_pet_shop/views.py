from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import *
from .forms import *

# Create your views here.
class Unidades (ListView):
    model = Unidade

class DetailUnidade (DetailView):
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

class DetailCliente (DetailView):
    # model = Cliente
    def get(self, request, pk, *args, **kwargs):
        cliente = get_object_or_404(Cliente, id=pk)
        pets = Pet.objects.filter(cliente=cliente.id)
        cliente.pets = pets
        print(cliente.pets)
        context = {'cliente': cliente}
        return render(request,'sistema_pet_shop/cliente_detail.html', context=context)


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

class Pets (ListView):
    model = Pet

class DetailPet (DetailView):
    model = Pet

def novoPet (request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    if request.method == 'POST':
        form = PetForm(request.POST)
        # form.fields['cliente'].initial =  cliente.id
        if form.is_valid():
            form.save()
            return redirect('/detail-cliente/' + str(cliente.id))
    form = PetForm()
    form.fields['cliente'].initial =  cliente.id

    return render(request,'novo_pet.html',{'form': form})