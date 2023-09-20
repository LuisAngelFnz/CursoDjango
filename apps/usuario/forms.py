from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            # 'password',
            'email',
        ]

        labels = {
            'first_name'  : 'Nombre',
            'last_name'   : 'Apellidos',
            'user_name'   : 'Login',
            'password'    : 'Contraseña',
            'email'       : 'Correo electronico'
        }