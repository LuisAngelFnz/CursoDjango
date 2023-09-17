from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from apps.adopcion.models import Solicitud,Persona
from apps.adopcion.forms  import SolicitudForm, PersonaForm
# Create your views here.

def index_adopcion(request):
    return HttpResponse('Hola Mundo desde la app adopcion')

class SolicitudBase:
    model = Solicitud
    success_url   = reverse_lazy('adopcion:listar_solicitud')

class SolicitudList(SolicitudBase, ListView):
    template_name = 'tadopcion/solicitud_listar.html'

class SolicitudCU(SolicitudBase):    
    template_name = 'tadopcion/solicitud_form.html'
    form_class    = SolicitudForm
    form_persona  = PersonaForm
    

class SolicitudCreate(SolicitudCU,CreateView):
    
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

class SolicitudUpdate(SolicitudCU, UpdateView):
    model_persona = Persona
    
    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        solicitud_id  = self.kwargs.get('pk', 0)
        solicitud     = self.model.objects.get(id=solicitud_id)
        persona       = self.model_persona.objects.get(id=solicitud.persona_id) #type: ignore
        if 'form' not in context:
            context['form'] = self.form_class() #type: ignore
        
        if 'frm_persona' not in context:
            context['frm_persona'] = self.form_persona(instance=persona)
        
        context['id'] = solicitud_id
        return context
     
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        solicitud_id = kwargs['pk']
        solicitud = self.model.objects.get(id=solicitud_id)
        persona = self.model_persona.objects.get(id=solicitud.persona_id) #type: ignore
        frm_solicitud = self.form_class(request.POST, instance=solicitud) #type: ignore
        frm_persona = self.form_persona(request.POST, instance=persona)
        if frm_solicitud.is_valid() and frm_persona.is_valid():
            frm_solicitud.save() #type: ignore
            frm_persona.save()
            # return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(SolicitudBase,DeleteView):
    template_name = 'tadopcion/solicitud_delete.html'
