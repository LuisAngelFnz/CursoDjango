from django.urls import path
from apps.adopcion.views import index_adopcion

from apps.adopcion import views

app_name = 'adopcion'

urlpatterns = [
    path('', views.index_adopcion),
    path('solicitud', views.SolicitudCreate.as_view(), name='solicitud'),
    path('solicitud/listar', views.SolicitudList.as_view(), name='listar_solicitud'),
    path('solicitud/editar/<int:pk>', views.SolicitudUpdate.as_view(), name='editar_solicitud'),
    path('solicitud/eliminar/<int:pk>', views.SolicitudDelete.as_view(), name='eliminar_solicitud')
]
