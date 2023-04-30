# views.py

from django.shortcuts import render


def menu_principal(request):
    return render(request, 'pqrs/menu.html')


def solicitudes(request):
    return render(request, 'pqrs/solicitudes.html')


def editor(request):
    return render(request, 'pqrs/editor.html')
