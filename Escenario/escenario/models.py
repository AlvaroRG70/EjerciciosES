from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electrónico = models.CharField(max_length=100, unique=True, blank=True)
    contraseña = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField()
    
    
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    ESTADIO = [
        ("PE","Pendiente"),
        ("PR","Progreso"),
        ("CO","Completada")
    ]
    estadio = models.CharField(max_length=2, choices=ESTADIO)
    completada = models.BooleanField()
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="creador2")
    usuario = models.ManyToManyField(Usuario, through="AsignacionTarea", related_name="usuario2")
    
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuarios = models.ManyToManyField(Usuario, through="ProyectoAsignado",related_name="usuarios")
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name="creador")
    tareas = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True, blank=True)
    tareas = models.ManyToManyField(Tarea, through="EtiquetaAsociada")
    
    

    

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField()
    autor = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    tarea = models.OneToOneField(Tarea, on_delete=models.CASCADE)




class ProyectoAsignado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
class AsignacionTarea(models.Model):
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    
    
    
class EtiquetaAsociada(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)

