from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import RegistroUsuario

app_name = 'usuario'

urlpatterns = [
    path('registrar', login_required(RegistroUsuario.as_view()), name='registrar_usuario')
]
