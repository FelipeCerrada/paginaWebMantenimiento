from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import ExcelUploadForm
import pandas as pd


def lista_mantenimientos(request):
    mantenimientos = Matriz.objects.all()
    return render(request, 'lista_mantenimientos.html', {'mantenimientos': mantenimientos})


# Marca temporal	
# fecha	
# Marca temporal	
# Operario	
# Hs	
# Actividad	
# Matrices	
# VW	
# GM	
# FIAT	
# RENAULT	
# ACTIVIDAD EN TALLER O EN PRENSA	
# componente con desgaste o rotura del mismo	
# Observaciones	
# Estado	
# Actividad Cerrada	
# AÑO	
# MES	
# EWO	
# ID	
# FECHA	
# EVENTOS



def cargar_excel(request):
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Leer el archivo cargado
            archivo_excel = request.FILES['archivo_excel']
            try:
                # Leer datos usando pandas
                data = pd.read_excel(archivo_excel, 'DESCARGA_CARGA_DIARIA')



                # Insertar datos en la base de datos
                for _, fila in data.iterrows():
                    Matriz.objects.create(
                        nombre=fila['Matrices'],
                        ubicacion="fila['ubicacion']",
                        tipo="TIPO",
                        fabricante="fila['fabricante']",
                        capacidad_golpes=100,
                        cont_golpes_actual=50
                        
                    )

                return HttpResponse("¡Datos importados exitosamente!")
            except Exception as e:
                return HttpResponse(f"Ocurrió un error: {e}")
    else:
        form = ExcelUploadForm()

    return render(request, "cargar_excel.html", {"form": form})
