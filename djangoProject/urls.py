"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.shortcuts import redirect

from pqrs import views
from pqrs.views import menu_principal, solicitudes, editor, classify_polarity

urlpatterns = [
    path('', lambda request: redirect('/menu/')),
   # path('classify/', classify_polarity, name='classify_polarity'),

    path('admin/', admin.site.urls),
    path('menu/', menu_principal),
    path('menu/solicitudes.html', solicitudes),
    path('menu/editor.html', editor),
    path('menu/menu.html', menu_principal),

    path('menu/classify_polarity', classify_polarity, name='classify_polarity'),
   # path('menu/guardar_datos', guardar_datos, name='guardar_datos'),

]
