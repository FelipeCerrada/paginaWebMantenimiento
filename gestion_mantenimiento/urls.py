from django.urls import path
from . import views

urlpatterns = [
    path('lista_mantenimientos/', views.lista_mantenimientos, name='lista_mantenimientos'),
    path('cargar_excel/', views.cargar_excel, name='cargar_excel'),
]
