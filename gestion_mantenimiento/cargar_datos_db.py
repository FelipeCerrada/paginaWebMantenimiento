

def crear_datos_db():
    #from models import Matriz, Tecnico, TipoMantenimiento, Repuesto, Herramienta, OrdenTrabajo, TecnicosPorOT, RepuestosPorOT, HerramientasPorOT, HistorialMantenimiento
    from gestion_mantenimiento.models import (
        Matriz,
        Tecnico,
        TipoMantenimiento,
        Repuesto,
        Herramienta,
        OrdenTrabajo,
        TecnicosPorOT,
        RepuestosPorOT,
        HerramientasPorOT,
        HistorialMantenimiento
    )
    from datetime import date, timedelta
    import random

    # Crear matrices
    matrices = [
        Matriz(nombre="Matriz A", ubicacion="Planta 1", tipo="Estampado", fabricante="ABC Corp", capacidad_golpes=5000, cont_golpes_actual=300),
        Matriz(nombre="Matriz B", ubicacion="Planta 2", tipo="Estampado", fabricante="XYZ Ltd", capacidad_golpes=10000, cont_golpes_actual=800),
    ]
    Matriz.objects.bulk_create(matrices)

    # Crear técnicos
    tecnicos = [
        Tecnico(nombre="Juan Pérez", especialidad="Correctivo", disponibilidad="Disponible"),
        Tecnico(nombre="Carlos Gómez", especialidad="Preventivo", disponibilidad="Ocupado"),
        Tecnico(nombre="María López", especialidad="Mejora", disponibilidad="Disponible"),
    ]
    Tecnico.objects.bulk_create(tecnicos)

    # Crear tipos de mantenimiento
    tipos_mantenimiento = [
        TipoMantenimiento(descripcion="Preventivo"),
        TipoMantenimiento(descripcion="Correctivo"),
        TipoMantenimiento(descripcion="Mejora"),
    ]
    TipoMantenimiento.objects.bulk_create(tipos_mantenimiento)

    # Crear repuestos
    repuestos = [
        Repuesto(nombre="Tornillo A", descripcion="Tornillo de alta resistencia", cantidad_disponible=100, unidad_medida="piezas"),
        Repuesto(nombre="Engranaje B", descripcion="Engranaje estándar", cantidad_disponible=50, unidad_medida="piezas"),
    ]
    Repuesto.objects.bulk_create(repuestos)

    # Crear herramientas
    herramientas = [
        Herramienta(nombre="Llave Inglesa", descripcion="Llave para ajuste", cantidad_disponible=10),
        Herramienta(nombre="Destornillador", descripcion="Juego de destornilladores", cantidad_disponible=15),
    ]
    Herramienta.objects.bulk_create(herramientas)

    # Crear órdenes de trabajo
    matriz1 = Matriz.objects.first()
    tecnico1 = Tecnico.objects.first()
    tipo_mantenimiento_preventivo = TipoMantenimiento.objects.get(descripcion="Preventivo")

    ordenes_trabajo = [
        OrdenTrabajo(
            matriz=matriz1,
            tipo_mantenimiento=tipo_mantenimiento_preventivo,
            estado="pendiente",
            prioridad="alta",
            fecha_planificada=date.today() + timedelta(days=7),
            fecha_realizada=None,
            golpes_a_realizar=1000
        )
    ]
    OrdenTrabajo.objects.bulk_create(ordenes_trabajo)

    # Asociar técnicos a órdenes de trabajo
    orden1 = OrdenTrabajo.objects.first()
    tecnico2 = Tecnico.objects.get(nombre="María López")
    TecnicosPorOT.objects.create(orden_trabajo=orden1, tecnico=tecnico1)
    TecnicosPorOT.objects.create(orden_trabajo=orden1, tecnico=tecnico2)

    # Asociar repuestos y herramientas a órdenes de trabajo
    repuesto1 = Repuesto.objects.first()
    herramienta1 = Herramienta.objects.first()
    RepuestosPorOT.objects.create(orden_trabajo=orden1, repuesto=repuesto1, cantidad_usada=10)
    HerramientasPorOT.objects.create(orden_trabajo=orden1, herramienta=herramienta1, cantidad_usada=2)

    # Crear historial de mantenimiento
    HistorialMantenimiento.objects.create(
        orden_trabajo=orden1,
        fecha=date.today(),
        observaciones="Mantenimiento preventivo realizado con éxito.",
        mttr_horas=2.5,
        mtbf_golpes=1500
    )

    print("¡Datos de ejemplo cargados con éxito!")

crear_datos_db()