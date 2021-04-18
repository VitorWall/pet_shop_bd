from django.shortcuts import render , redirect, get_object_or_404
from django.views.generic import DeleteView, ListView
from .models import *

# Create your views here.
class Home (ListView):
    model = Unidade

