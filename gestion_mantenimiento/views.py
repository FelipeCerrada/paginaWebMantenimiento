from django.shortcuts import render
from .models import Mantenimiento

def lista_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'gestion_mantenimiento/lista_mantenimientos.html', {'mantenimientos': mantenimientos})

