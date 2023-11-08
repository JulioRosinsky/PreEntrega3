from django.urls import path
from AppCoder.views import *
from . import views

urlpatterns = [
    path('',Inicio, name='Inicio'), 
    path('estudiantes/', Estudiantes, name="estudiante"),
    path('profesores/', Profesores, name="profesor"),
    path('entregables/', Entregables, name='entregables'), 
    
    path('entregablesForm/',EntregablesForm, name='entregablesForm'),
    path('estudianteForm/',EstudianteForm, name='estudianteForm'),
    path('profesorForm/', ProfesorForm, name='profesorForm'),
]