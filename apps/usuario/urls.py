from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import RegistroUsuario, UserAPI

app_name = 'usuario'

urlpatterns = [
    path('registrar', login_required(RegistroUsuario.as_view()), name='registrar_usuario'),
    path('api', UserAPI.as_view(), name='usuario_api')
]
