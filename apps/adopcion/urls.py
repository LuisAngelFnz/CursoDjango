from django.urls import path
from apps.adopcion.views import index_adopcion

from apps.adopcion.views import SolicitudList, SolicitudCreate
app_name = 'adopcion'

urlpatterns = [
    path('', index_adopcion),
    path('solicitud', SolicitudCreate.as_view(), name='solicitud'),
    path('listar', SolicitudList.as_view(), name='listar_solicitud'),
]
