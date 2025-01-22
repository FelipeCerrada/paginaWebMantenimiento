from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    propietario = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Matriz(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    tipo_matriz = models.CharField(max_length=50, choices=[('Progresiva', 'Detalle Progresiva'), ('Transfer', 'Detalle Transfer')])
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_equipo


class Operario(models.Model):
    nombre = models.TextField()
    legajo = models.IntegerField()
    fecha_ingreso = models.DateField()
    
    def __str__(self):
        return self.nombre
    

class Mantenimiento(models.Model):
    nombre_equipo = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_mantenimiento = models.DateField()
    tipo_mantenimiento = models.CharField(max_length=50, choices=[('Preventivo', 'Preventivo'), ('Correctivo', 'Correctivo')])
    duracion_horas = models.FloatField() 
    realizado_por = models.ForeignKey(Operario, on_delete=models.CASCADE)
    
    def __str__(self):

        return self.descripcion +' - '+ str(self.fecha_mantenimiento)


