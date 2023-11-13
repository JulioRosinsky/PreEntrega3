from django.shortcuts import render, redirect
from .forms import ProfesorForm, EstudianteForm, EntregablesForm, BusquedaProfesorForm, BusquedaEstudianteForm
from .models import Profesor, Estudiante, Entregables
# Create your views here.

def Inicio(request):
    return render(request, 'AppCoder/index.html')

def Entregables(request):
    return render(request, 'AppCoder/entregables.html')

def Estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def Profesores(request):
    return render(request, 'AppCoder/profesores.html')

def formularioEstudiante(request):
    
    data = {
        'form': EstudianteForm
    }
    
    if request.method == 'POST':
        formulario = EstudianteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario
            
        
    return render(request, 'AppCoder/estudianteform.html', data)
 
def formularioProfesor(request):
    
    data = {
        'form': ProfesorForm
    }
    
    if request.method == 'POST':
        formulario = ProfesorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario
        
    return render(request, 'AppCoder/profesoresform.html', data)

def formularioEntregables(request):
    data = {
        'form': EntregablesForm()
    }
    
    if request.method == 'POST':
        formulario = EntregablesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario
        
    return render(request, 'AppCoder/entregablesForm.html', data)


def buscar_profe(request):
    if request.method == 'POST':
        form = BusquedaProfesorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']

            profesor = Profesor.objects.filter(nombre=nombre, apellido=apellido).first()
            estudiante = Estudiante.objects.filter(nombre=nombre, apellido=apellido).first()

            return render(request, 'resultados_busqueda.html', {'profesor': profesor, 'estudiante': estudiante})

    else:
        form = BusquedaProfesorForm()

    return render(request, 'buscar.html', {'form': form})

def buscar_estudiante(request):
    if request.method == 'POST':
        form = BusquedaEstudianteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']

            profesor = Profesor.objects.filter(nombre=nombre, apellido=apellido).first()
            estudiante = Estudiante.objects.filter(nombre=nombre, apellido=apellido).first()

            return render(request, 'resultados.html', {'profesor': profesor, 'estudiante': estudiante})

    else:
        form = BusquedaEstudianteForm()

    return render(request, 'buscar.html', {'form': form})