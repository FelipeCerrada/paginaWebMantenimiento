from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mantenimientos, name='lista_mantenimientos'),
]
