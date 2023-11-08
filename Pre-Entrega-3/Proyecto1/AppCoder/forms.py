from django import forms

class EstudianteForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    email = forms.EmailField(label = 'Email')
    
    
class ProfesorForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    email = forms.EmailField(label = 'Email')
    edad = forms.IntegerField(label='Edad')
    
class EntregablesForm(forms.Form):
    nombre = forms.CharField(label='Nombre de la tarea')
    materia = forms.CharField(label='Materia') 
    fecha_de_entrega = forms.DateField(label='Fecha de Entrega')
    
    