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

class FuncionarioForm (forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"
        widgets = {'unidade': forms.HiddenInput()}

