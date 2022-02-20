from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.mascota.forms import MascotaForm

from apps.mascota.models import Mascota

# Create your views here.

def index_mascota(request):
    return render(request, 'tmascota/index.html')

def mascota_view(request):
    print('method received: {}'.format(request.method))
    if str(request.method).lower() != 'post':
        form = MascotaForm()
    else:
        form = MascotaForm(request.POST)

        print('Reading form, is_valid: {}'.format(form.is_valid()))

        if form.is_valid():
            form.save()
            print('redirect to index mascota')
            return redirect('mascota:index')

    return render(request, 'tmascota/mascota_form.html', {'form':form})

def listar_mascotas(request):
    all_mascotas = Mascota.objects.all()

    return render(request, 'tmascota/mascota_list.html', {'mascotas':all_mascotas})
