from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from apps.adopcion.models import Solicitud
from apps.adopcion.forms  import SolicitudForm, PersonaForm
# Create your views here.

def index_adopcion(request):
    return HttpResponse('Hola Mundo desde la app adopcion')

class SolicitudList(ListView):
    model = Solicitud
    template_name = 'tadopcion/solicitud_listar.html'

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'tadopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('tadopcion:solicitud_listar.html')
    
    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form2=form2)
            )