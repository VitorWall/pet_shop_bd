from django import forms
from .models import *

class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = "__all__" # ['nome', 'especie', 'raca', 'sexo']
        widgets = {'cliente': forms.HiddenInput()}

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = "__all__"

class AcomodacaoForm(forms.ModelForm):
    class Meta:
        model = Acomodacao
        fields = "__all__"
        widgets = {'unidade': forms.HiddenInput()}
        
class FuncionarioForm (forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"
        widgets = {'unidade': forms.HiddenInput()}

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = "__all__"
        widgets = {'unidade': forms.HiddenInput()}

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = "__all__"
        widgets = {'pet': forms.HiddenInput()}

class EstadiaForm(forms.ModelForm):
    class Meta:
        model = Estadia
        fields = "__all__"
        widgets = {'pet': forms.HiddenInput()}

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
        widgets = {'unidade': forms.HiddenInput()}
