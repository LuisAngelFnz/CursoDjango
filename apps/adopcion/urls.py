from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.adopcion.views import index_adopcion

from apps.adopcion import views

app_name = 'adopcion'

urlpatterns = [
    path('', login_required(views.index_adopcion)),
    path('solicitud', login_required(views.SolicitudCreate.as_view()), name='solicitud'),
    path('solicitud/listar', login_required(views.SolicitudList.as_view()), name='listar_solicitud'),
    path('solicitud/editar/<int:pk>', login_required(views.SolicitudUpdate.as_view()), name='editar_solicitud'),
    path('solicitud/eliminar/<int:pk>', login_required(views.SolicitudDelete.as_view()), name='eliminar_solicitud')
]
