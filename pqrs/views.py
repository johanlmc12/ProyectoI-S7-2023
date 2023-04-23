# views.py

from django.shortcuts import render
from .models import Solicitud


def lista_solicitudes(request):
    return render(request, 'pqrs/menu.html')



