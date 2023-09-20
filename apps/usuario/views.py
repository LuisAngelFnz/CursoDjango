from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import UsuarioForm

class RegistroUsuario(CreateView):
    model         = User
    template_name = 'tusuario/registrar.html'
    form_class    = UsuarioForm
    success_url   = reverse_lazy('mascota:listar_mascotas')
