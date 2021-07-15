from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from .forms import LoginHenryForm
from .models import Vehiculo,Marca
from time import timezone
# Create your views here.

class LoginView(FormView):
    template_name='views/auth/login.html'
    form_class = LoginHenryForm
    success_url = reverse_lazy('app:vehiculos_all')

class VehiculoListView(ListView):
    template_name='views/vehiculo/all.html'
    model = Vehiculo

class MarcaListView(ListView):
    template_name='views/marca/all.html'
    model = Marca