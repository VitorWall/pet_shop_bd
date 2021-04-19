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

