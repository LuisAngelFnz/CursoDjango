from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.mascota.views import (
    indexMascota,
    # mascotaNueva,
    # listarMascotas,
    # mascotaEditar,
    # mascotaEliminar,
    MascotaList,
    MascotaCreate,
    MascotaUpdate,
    MascotaDelete,
    WSMascotaList
)

app_name = 'mascota'

urlpatterns = [
    path('', indexMascota, name='mascota_index'),
    path('nueva',   login_required(MascotaCreate.as_view()), name='mascota_nueva'),
    path('listar', login_required(MascotaList.as_view()), name='listar_mascotas'),
    path('editar/<int:pk>',  login_required(MascotaUpdate.as_view()), name='editar_mascota'),
    path('eliminar/<int:pk>',  login_required(MascotaDelete.as_view()), name='eliminar_mascota'),
    path('ws/all', WSMascotaList, name='ws_all')
]
