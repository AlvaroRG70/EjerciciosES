from django.shortcuts import render
from escenario.models import Proyecto, Tarea, AsignacionTarea,Comentario

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador","tareas").prefetch_related("usuarios")
    return render(request, "proyecto/lista.html", {"lista_proyectos":proyectos})

def listar_tareas(request):
    tareas = Tarea.objects.select_related("creador").prefetch_related("usuario")
    return render(request, "tarea/listatarea.html", {"tareas_mostrar":tareas})

def lista_usuarios_tarea(request):
    asig_tareas= AsignacionTarea.objects.select_related("usuario")
    asig_tareas = asig_tareas.order_by("fecha_asignacion")
    return render(request, "asignaciontarea/lista.html", {"tarea_fecha":asig_tareas})

def dame_tareas(request, texto_obs):
    tareas = AsignacionTarea.objects.select_related("tarea")
    tareas = tareas.filter(observaciones__contains = texto_obs)
    return render(request, "asignaciontarea/tareatext.html", {"dame_tareas_escenario":tareas})

def proyectos_completados(request, anyo1, anyo2):
    tareas = Tarea.objects.filter(fecha_creacion__year__gt=anyo1).filter(fecha_creacion__year__lt=anyo2).filter(estadio="CO")
    return render(request, "tarea/proyectofecha.html", {"dame_proyectos_completados":tareas})

def dame_ultimo_usuario(request):
    usuarios = Comentario.objects.order_by("-fecha_comentario")[:1].get()
    return render(request, "comentario/comentario.html",{"ultimo_usuario":usuarios})
