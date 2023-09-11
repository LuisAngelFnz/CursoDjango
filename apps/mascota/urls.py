from django.urls import path

from apps.mascota.views import (
    indexMascota,
    mascotaNueva,
    listarMascotas,
    mascotaEditar,
    mascotaEliminar
)

app_name = 'mascota'

urlpatterns = [
    path('', indexMascota, name='index'),
    path('nueva',   mascotaNueva, name='mascota_nueva'),
    path('listar', listarMascotas, name='listar_mascotas'),
    path('editar/<int:id_mascota>',  mascotaEditar, name='editar_mascota'),
    path('eliminar/<int:id_mascota>',  mascotaEliminar, name='eliminar_mascota'),
]
