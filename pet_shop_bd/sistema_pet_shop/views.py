from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView, ListView
from .models import *
from .forms import *

# Create your views here.
class Home (ListView):
    model = Unidade

def novaUnidade (request):
    if request.method == 'POST':
        form = UnidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sistema_pet_shop:home')
    form = UnidadeForm()

    return render(request,'nova_unidade.html',{'form': form})
