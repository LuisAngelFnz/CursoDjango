from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    model         = Solicitud
    template_name = 'tadopcion/solicitud_form.html'
    form_class    = SolicitudForm
    form_persona  = PersonaForm
    success_url   = reverse_lazy('adopcion:listar_solicitud')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        frm_solicitud = self.form_class(request.POST) # type: ignore
        frm_persona   = self.form_persona(request.POST) # type: ignore
        if frm_solicitud.is_valid() and frm_persona.is_valid():
            solicitud = frm_solicitud.save(commit=False)  # type: ignore
            solicitud.persona = frm_persona.save() # type: ignore
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(
                    form=frm_solicitud,
                    frm_persona=frm_persona
                )
            )
    
    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET) # type: ignore
        
        if 'frm_persona' not in context:
            context['frm_persona'] = self.form_persona(self.request.GET) # type: ignore
        
        return context
