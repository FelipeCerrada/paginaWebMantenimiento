from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    dueño = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Matriz(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    capacidad_golpes = models.PositiveIntegerField(blank=True, null=True)
    cont_golpes_actual = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class ProyectoPorCliente(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.proyecto.nombre} (De {self.cliente.nombre})"

class MatricesPorProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.matriz.nombre} (De {self.proyecto.nombre})"


class Tecnico(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoMantenimiento(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class Repuesto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    cantidad_disponible = models.PositiveIntegerField()
    unidad_medida = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Herramienta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    cantidad_disponible = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class OrdenTrabajo(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En Curso'),
        ('completada', 'Completada'),
    ]

    PRIORIDADES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]

    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE, related_name="ordenes_trabajo")
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE, related_name="ordenes_trabajo")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='media')
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_planificada = models.DateField()
    fecha_realizada = models.DateField(null=True, blank=True)
    duracion_horas = models.FloatField(null=True, blank=True)
    golpes_a_realizar = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Orden {self.id} - {self.estado}"

class TecnicosPorOT(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="tecnicos")
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name="ordenes_asignadas")

    class Meta:
        unique_together = ('orden_trabajo', 'tecnico')

    def __str__(self):
        return f"{self.tecnico.nombre} en OT {self.orden_trabajo.id}"

class RepuestosPorOT(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="repuestos_usados")
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE, related_name="usos")
    cantidad_usada = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad_usada}x {self.repuesto.nombre} (OT {self.orden_trabajo.id})"

class HerramientasPorOT(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="herramientas_usadas")
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE, related_name="usos")
    cantidad_usada = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad_usada}x {self.herramienta.nombre} (OT {self.orden_trabajo.id})"

class HistorialMantenimiento(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name="historial")
    fecha = models.DateField()
    observaciones = models.TextField(null=True, blank=True)
    mttr_horas = models.FloatField(null=True, blank=True)
    mtbf_golpes = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Historial para OT {self.orden_trabajo.id}"
