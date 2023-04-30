# views.py

from django.shortcuts import render
from .models import Solicitud
from django.contrib.auth.views import PasswordResetView


def lista_solicitudes(request):
    return render(request, 'pqrs/menu.html')


def admin(request):
    return render(request, 'admin/base_site.html')


