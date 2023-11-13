from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30,)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Entregables(models.Model):
    nombre_de_la_tarea = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    
    def __str__(self):
        return self.nombre_de_la_tarea
    
class BusquedaProfesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
class BusquedaEstudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    