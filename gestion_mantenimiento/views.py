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

#	CLIENTE
# 	PROYECTO
# 	MATRIZ
#  	IMAGEN
# 	EX
#  NRO MATRIZ	DESCRIPCION	NICK NAME	VS / OB	"PRENSA
#(S/ ARCHIVO MARI)"	PRENSA 2	-	PRENSA	Constructor	Size (Ton)	Type	Process	Unwinder	Working Height Max	Working Height Min	Regulate	Stroke [mm]	Bolster	LISTA DE MATERIALES	RUTA


def cargar_clientes(data):
    # Insertar datos PROYECTOS en la base de datos
    for _, fila in data.iterrows():
        Cliente.objects.create(
            nombre=fila['CLIENTE'],
            grupo='STELLANTIS',
            
        )

def cargar_matrices(data):
    # Insertar datos MATRICES en la base de datos
    for _, fila in data.iterrows():
        Matriz.objects.create(
            nombre=fila['CLIENTE'],
            ubicacion="fila['ubicacion']",
            tipo="TIPO",
            capacidad_golpes=100,
            cont_golpes_actual=50
            
        )


def cargar_excel(request):
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Leer el archivo cargado
            archivo_excel = request.FILES['archivo_excel']
            try:
                # Leer datos usando pandas
                data = pd.read_excel(archivo_excel, 'DB')

                cargar_clientes(data)
                cargar_matrices(data)
   
                return HttpResponse("¡Datos importados exitosamente!")
            except Exception as e:
                return HttpResponse(f"Ocurrió un error: {e}")
    else:
        form = ExcelUploadForm()

    return render(request, "cargar_excel.html", {"form": form})
