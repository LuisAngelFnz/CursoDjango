from django.urls import path

from apps.mascota.views import (index_mascota,
                                mascota_view,
                                listar_mascotas)

app_name = 'mascota'

urlpatterns = [
    path('', index_mascota, name='index'),
    path('NuevamMascota', mascota_view, name='mascota_nueva'),
    path('listarMascotas', listar_mascotas, name='listar_mascotas')
]
