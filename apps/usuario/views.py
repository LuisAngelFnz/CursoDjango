import json

from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.forms import UsuarioForm
from apps.usuario.serializers import UserSerializer
from rest_framework.views import APIView
from django.http import HttpResponse

class RegistroUsuario(CreateView):
    model         = User
    template_name = 'tusuario/registrar.html'
    form_class    = UsuarioForm
    success_url   = reverse_lazy('mascota:listar_mascotas')


class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        users = User.objects.all()
        response = self.serializer(users, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')
