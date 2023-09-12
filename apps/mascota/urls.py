from django.urls import path

from apps.mascota.views import (
    indexMascota,
    mascotaNueva,
    listarMascotas,
    mascotaEditar,
    mascotaEliminar,
    MascotaList,
    MascotaCreate,
    MascotaUpdate,
    MascotaDelete
)

app_name = 'mascota'

urlpatterns = [
    path('', indexMascota, name='mascota_index'),
    path('nueva',   MascotaCreate.as_view(), name='mascota_nueva'),
    path('listar', MascotaList.as_view(), name='listar_mascotas'),
    path('editar/<int:pk>',  MascotaUpdate.as_view(), name='editar_mascota'),
    path('eliminar/<int:pk>',  MascotaDelete.as_view(), name='eliminar_mascota'),
]
