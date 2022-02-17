from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_adopcion(__request):
    return HttpResponse('Hola Mundo desde la app adopcion')
