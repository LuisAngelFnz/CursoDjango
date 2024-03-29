
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota


def WSMascotaList(request):
    return HttpResponse(
        serializers.serialize(
            'json',
            Mascota.objects.all(),
            fields=['nombre','sexo','edad']
        ),
        content_type='application/json'
    )

def indexMascota(request):
    return render(request, 'tmascota/index.html')

def mascotaNueva(request):
    print('method received: {}'.format(request.method))
    if request.method != 'POST':
        form = MascotaForm()
    else:
        form = MascotaForm(request.POST)

        print('Reading form, is_valid: {}'.format(form.is_valid()))
        if form.is_valid():
            form.save()
            print('redirect to index mascota')
            return redirect('mascota:listar_mascotas')

    return render(request, 'tmascota/mascota_form.html', {'form':form})

def listarMascotas(request):
    all_mascotas = Mascota.objects.all()
    return render(request, 'tmascota/mascota_list.html', {'mascotas':all_mascotas})

def mascotaEditar(request, id_mascota):
    try:
        objmascota  = Mascota.objects.get(id=id_mascota)
    except Mascota.DoesNotExist:
        print('Mascota no encontrada con id: {}'.format(id_mascota))
        return redirect('mascota:listar_mascotas')
        
    if request.method == 'GET':
        form = MascotaForm(instance=objmascota)
    else:
        form = MascotaForm(request.POST, instance=objmascota)
        if form.is_valid():
            form.save()
            return redirect('mascota:listar_mascotas')
    
    return render(request, 'tmascota/mascota_form.html', {'form':form})

def mascotaEliminar(request, id_mascota):
    try:
        objmascota  = Mascota.objects.get(id=id_mascota)
    except Mascota.DoesNotExist:
        print('Mascota no encontrada con id: {}'.format(id_mascota))
        return redirect('mascota:listar_mascotas')
        
    if request.method == 'POST':
        objmascota.delete()
        return redirect('mascota:listar_mascotas')
    
    return render(request, 'tmascota/mascota_delete.html', {'mascota':objmascota})

class MascotaModel:
    model = Mascota

class MascotaList(MascotaModel, ListView):
    template_name = 'tmascota/mascota_list.html'
    paginate_by = 2

class MascotaCRUD(MascotaModel):
    form_class    = MascotaForm
    template_name = 'tmascota/mascota_form.html'
    success_url   = reverse_lazy('mascota:listar_mascotas')

class MascotaCreate(MascotaCRUD, CreateView):
    pass

class MascotaUpdate(MascotaCRUD, UpdateView):
    pass

class MascotaDelete(DeleteView):
    model = Mascota
    template_name =  'tmascota/mascota_delete.html'
    success_url   = reverse_lazy('mascota:listar_mascotas')