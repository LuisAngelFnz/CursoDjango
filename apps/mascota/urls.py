from django.urls import path
from apps.mascota.views import index_mascota

app_name = 'mascota'

urlpatterns = [
    path('', index_mascota),
]
