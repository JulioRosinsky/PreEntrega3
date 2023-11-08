from django.shortcuts import render
from .forms import ProfesorForm, EstudianteForm, EntregablesForm
# Create your views here.

def Inicio(request):
    return render(request, 'AppCoder/index.html')

def Entregables(request):
    return render(request, 'AppCoder/entregables.html')

def Estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def Profesores(request):
    return render(request, 'AppCoder/profesores.html')

from AppCoder.forms import ProfesorForm, EstudianteForm, EntregablesForm
from django.shortcuts import render
from .forms import ProfesorForm, EstudianteForm, EntregablesForm

def formulario_profesores(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            pass 
    else:  
        form = ProfesorForm()
        
    return render(request, 'AppCoder/profesores.html', {'form': form})

def formulario_estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            pass 
    else:  
        form = EstudianteForm()
        
    return render(request, 'AppCoder/estudiantes.html', {'form': form})

def formulario_entregables(request):
    if request.method == 'POST':
        form = EntregablesForm(request.POST)
        if form.is_valid():
            pass 
    else:  
        form = EntregablesForm()
        
    return render(request, 'AppCoder/entregables.html', {'form': form})