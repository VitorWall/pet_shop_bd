from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import *
from .forms import *

# UNIDADE ---------------------------------------------------------------------------

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
    return redirect('sistema_pet_shop:unidades')

# CLIENTE ---------------------------------------------------------------------------

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

# PET ---------------------------------------------------------------------------

class Pets (ListView):
    model = Pet

class DetailPet (DetailView):
    # model = Pet
    def get(self, request, pk, *args, **kwargs):
        pet = get_object_or_404(Pet, id=pk)
        agendamentos = Agendamento.objects.filter(pet=pet.id)
        estadias = Estadia.objects.filter(pet=pet.id)
        pet.agendamentos = agendamentos
        pet.estadias = estadias
        context = {'pet': pet}
        return render(request,'sistema_pet_shop/pet_detail.html', context=context)

def novoPet (request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/detail-cliente/' + str(cliente.id))
    form = PetForm()
    form.fields['cliente'].initial =  cliente.id

    return render(request,'novo_pet.html',{'form': form})

def editPet (request, pk, template_name='sistema_pet_shop/edit_pet.html'):
    pet = get_object_or_404(Pet, id=pk)
    form = PetForm(request.POST or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('/detail-cliente/' + str(pet.cliente.id))
    return render(request, template_name, {'form':form})

def deletePet (request, pk, template_name=''):
    pet = get_object_or_404(Pet, id=pk)
    pet.delete()
    return redirect('/detail-cliente/' + str(pet.cliente.id))

# FUNCIONÁRIO ---------------------------------------------------------------------------

class Funcionarios (ListView):
    def get(self, request, pk, *args, **kwargs):
        unidade = get_object_or_404(Unidade, id=pk)
        funcionarios = Funcionario.objects.filter(unidade=unidade.id)
        funcionarios.unidade = unidade
        context = {'funcionarios': funcionarios}
        return render(request,'sistema_pet_shop/funcionario_list.html', context=context)

def novoFuncionario (request, pk):
    unidade = get_object_or_404(Unidade, id=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios/' + str(unidade.id))
    form = FuncionarioForm()
    form.fields['unidade'].initial =  unidade.id

    return render(request,'novo_funcionario.html',{'form': form})

def editFuncionario (request, pk, template_name='sistema_pet_shop/edit_funcionario.html'):
    funcionario = get_object_or_404(Funcionario, id=pk)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('/funcionarios/' + str(funcionario.unidade.id))
    return render(request, template_name, {'form':form})

def deleteFuncionario (request, pk, template_name=''):
    funcionario = get_object_or_404(Funcionario, id=pk)
    funcionario.delete()
    return redirect('/funcionarios/' + str(funcionario.unidade.id))

# SERVIÇO ---------------------------------------------------------------------------

class Servicos (ListView):
    model = Servico

def novoServico (request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistema_pet_shop:servicos')
    form = ServicoForm()

    return render(request,'novo_servico.html',{'form': form})

def editServico (request, pk, template_name='sistema_pet_shop/edit_servico.html'):
    servico = get_object_or_404(Servico, id=pk)
    form = ServicoForm(request.POST or None, instance=servico)
    if form.is_valid():
        form.save()
        return redirect('sistema_pet_shop:servicos')
    return render(request, template_name, {'form':form})

def deleteServico (request, pk, template_name=''):
    servico = get_object_or_404(Servico, id=pk)
    servico.delete()
    return redirect('/servicos')

# ACOMODAÇÃO ---------------------------------------------------------------------------

class Acomodacoes (ListView):
    def get(self, request, pk, *args, **kwargs):
        unidade = get_object_or_404(Unidade, id=pk)
        acomodacoes = Acomodacao.objects.filter(unidade=unidade.id)
        acomodacoes.unidade = unidade
        context = {'acomodacoes': acomodacoes}
        return render(request,'sistema_pet_shop/acomodacao_list.html', context=context)

def novaAcomodacao (request, pk):
    unidade = get_object_or_404(Unidade, id=pk)
    if request.method == 'POST':
        form = AcomodacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/acomodacoes/'+ str(unidade.id))
    form = AcomodacaoForm()
    form.fields['unidade'].initial =  unidade.id

    return render(request,'nova_acomodacao.html',{'form': form})

def editAcomodacao (request, pk, template_name='sistema_pet_shop/edit_acomodacao.html'):
    acomodacao = get_object_or_404(Acomodacao, id=pk)
    form = AcomodacaoForm(request.POST or None, instance=acomodacao)
    if form.is_valid():
        form.save()
        return redirect('sistema_pet_shop:acomodacoes')
    return render(request, template_name, {'form':form})

def deleteAcomodacao (request, pk, template_name=''):
    acomodacao = get_object_or_404(Acomodacao, id=pk)
    acomodacao.delete()
    return redirect('/acomodacoes/' + str(acomodacao.unidade.id))

# AGENDAMENTO ---------------------------------------------------------------------------

class Agendamentos (ListView):
    model = Agendamento

def novoAgendamento (request, pk):
    pet = get_object_or_404(Pet, id=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/detail-pet/' + str(pet.id))
    form = AgendamentoForm()
    form.fields['pet'].initial =  pet.id

    return render(request,'novo_agendamento.html',{'form': form})

def editAgendamento (request, pk, template_name='sistema_pet_shop/edit_agendamento.html'):
    agendamento = get_object_or_404(Agendamento, id=pk)
    form = AgendamentoForm(request.POST or None, instance=agendamento)
    if form.is_valid():
        form.save()
        return redirect('/detail-pet/' + str(agendamento.pet.id))
    return render(request, template_name, {'form':form})

def deleteAgendamento (request, pk, template_name=''):
    agendamento = get_object_or_404(Agendamento, id=pk)
    agendamento.delete()
    return redirect('/detail-pet/' + str(agendamento.pet.id))

# ESTADIA ---------------------------------------------------------------------------

class estadias (ListView):
    model = Estadia

def novaEstadia (request, pk):
    pet = get_object_or_404(Pet, id=pk)
    if request.method == 'POST':
        form = EstadiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/detail-pet/' + str(pet.id))
    form = EstadiaForm()
    form.fields['pet'].initial =  pet.id

    return render(request,'nova_estadia.html',{'form': form})

def editEstadia (request, pk, template_name='sistema_pet_shop/edit_estadia.html'):
    agendamento = get_object_or_404(Agendamento, id=pk)
    form = AgendamentoForm(request.POST or None, instance=agendamento)
    if form.is_valid():
        form.save()
        return redirect('/detail-pet/' + str(agendamento.pet.id))
    return render(request, template_name, {'form':form})

def deleteEstadia (request, pk, template_name=''):
    estadia = get_object_or_404(Estadia, id=pk)
    estadia.delete()
    return redirect('/detail-pet/' + str(estadia.pet.id))

# SALA ---------------------------
def novaSala (request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistema_pet_shop:salas')
    form = SalaForm()

    return render(request,'nova_sala.html',{'form': form})

class Salas (ListView):
    # model = Sala
    def get(self, request, pk, *args, **kwargs):
        unidade = get_object_or_404(Unidade, id=pk)
        salas = Sala.objects.filter(unidade=unidade.id)
        salas.unidade = unidade
        context = {'salas': salas}
        return render(request,'sistema_pet_shop/sala_list.html', context=context)

def editSala (request, pk, template_name='sistema_pet_shop/edit_sala.html'):
    sala = get_object_or_404(Sala, id=pk)
    form = SalaForm(request.POST or None, instance=sala)
    if form.is_valid():
        form.save()
        return redirect('sistema_pet_shop:salas')
    return render(request, template_name, {'form':form})

def deleteSala (request, pk, template_name=''):
    sala = get_object_or_404(Sala, id=pk)
    sala.delete()
    return redirect('/salas')

# ESTOQUE---------------------
class Estoque (ListView):
    def get(self, request, pk, *args, **kwargs):
        unidade = get_object_or_404(Unidade, id=pk)
        estoque = Produto.objects.filter(unidade=unidade.id)
        estoque.unidade = unidade
        context = {'estoque': estoque}
        return render(request,'sistema_pet_shop/produto_list.html', context=context)
