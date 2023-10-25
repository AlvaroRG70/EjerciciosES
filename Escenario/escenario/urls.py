from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('proyectos/listar', views.listar_proyectos, name = "lista_proyectos"),
    path("tarea/listar", views.listar_tareas, name = "lista_tareas"),
    path("tarea/usuario_tarea", views.lista_usuarios_tarea, name = "usuario_lista_tarea"),
    path("escenario/tarea/<str:texto_obs>", views.dame_tareas, name = "dame_tareas_escenario"),
    path("proyectos/listar/<int:anyo1>/<int:anyo2>", views.proyectos_completados, name = "dame_proyectos_completados"),
    path("ult-usuario", views.dame_ultimo_usuario, name="ultimo_usuario"),
]
