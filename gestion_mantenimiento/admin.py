from django.contrib import admin
from .models import *


admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Tecnico)
admin.site.register(Matriz)
admin.site.register(ProyectoPorCliente)
admin.site.register(MatricesPorProyecto)
admin.site.register(TipoMantenimiento)
admin.site.register(Repuesto)
admin.site.register(Herramienta)
admin.site.register(OrdenTrabajo)
admin.site.register(TecnicosPorOT)
admin.site.register(RepuestosPorOT)
admin.site.register(HerramientasPorOT)
admin.site.register(HistorialMantenimiento)




