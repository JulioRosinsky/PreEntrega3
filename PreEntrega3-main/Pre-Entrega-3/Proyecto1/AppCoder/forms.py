from django import forms
from .models import Estudiante, Entregables,Profesor, BusquedaEstudiante, BusquedaProfesor

class EstudianteForm(forms.ModelForm):
    
    class Meta:
        model = Estudiante
        fields = '__all__'
    
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class EntregablesForm(forms.ModelForm):
    class Meta:
        model = Entregables
        fields = '__all__'

class BusquedaProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido']

class BusquedaEstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido']
