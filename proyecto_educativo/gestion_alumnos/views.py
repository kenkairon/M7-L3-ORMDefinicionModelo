from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm

# Create your views here.
def index(request):
    return render(request, 'gestion_alumnos/index.html')

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion_alumnos/lista_estudiantes.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'gestion_alumnos/crear_estudiante.html', {'form': form})