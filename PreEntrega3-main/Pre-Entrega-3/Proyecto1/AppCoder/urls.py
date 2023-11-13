from django.urls import path
from AppCoder.views import *
from . import views

urlpatterns = [
    path('',Inicio, name='Inicio'), 
    path('estudiantes/', Estudiantes, name="estudiante"),
    path('profesores/', Profesores, name="profesor"),
    path('entregables/', Entregables, name='entregables'), 
    path('formulario_profe/', formularioProfesor, name= 'profeform'),
    path('formulario_estudiante/', formularioEstudiante, name='studentform'),
    path('formulario_entregables/', formularioEntregables, name='tareasform'),
    path('buscar_profesor/', buscar_profe, name='buscar_profesor'),
    path('buscar_estudiante/', buscar_estudiante, name='buscar_estudiante'),
]