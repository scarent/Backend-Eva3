from django.shortcuts import render, redirect, get_object_or_404
from appAlumno.models import Alumno, Curso, Matricula
from appAlumno.forms import FormularioAlumno, FormularioCurso

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listarAlumnos(request):
    alumnos = Alumno.objects.all()
    data = {'alumnos':alumnos}
    return render(request, 'listadoAlumnos.html', data)

def registrarAlumnos(request):
    form = FormularioAlumno()
    if request.method == 'POST':
        form = FormularioAlumno(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/alumnos')
    else:
        form = FormularioAlumno()
    data = {'form':form}
    return render(request, 'registrarAlumnos.html', data)

def eliminarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('/alumnos')

def actualizarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    form = FormularioAlumno(instance=alumno)
    if request.method == 'POST':
        form = FormularioAlumno(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('/alumnos')
    else:
        form = FormularioAlumno(instance=alumno)
    data = {'form':form}
    return render(request, 'registrarAlumnos.html', data)

# Cursos
def listadoCursos(request):
    cursos = Curso.objects.all()
    data = {'cursos':cursos}
    return render(request, 'listadoCursos.html', data)

def agregarCurso(request):
    form = FormularioCurso()
    if request.method == 'POST':
        form = FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cursos')
    else:
        form = FormularioCurso()
    data = {'form':form}
    return render(request, 'agregarCurso.html', data)

def eliminarCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/cursos')

def actualizarCurso(request, id):
    curso = Curso.objects.get(id=id)
    form = FormularioCurso(instance=curso)
    if request.method == 'POST':
        form = FormularioCurso(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('/cursos')
    else:
        form = FormularioCurso(instance=curso)
    data = {'form':form}
    return render(request, 'agregarCurso.html', data)

#ManyToMany (Alumno y Curso)
def cursos_de_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    cursos = alumno.cursos.all()
    data = {'alumno': alumno, 'cursos': cursos}
    return render(request, 'cursosDeAlumno.html', data)

def alumnos_de_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    # Obtener los alumnos matriculados en el curso  -  (a través de la tabla Matricula)
    matriculas = Matricula.objects.filter(curso=curso)
    alumnos = [matricula.alumno for matricula in matriculas]  # Obtener la lista de alumnos
    data = {'curso': curso, 'alumnos': alumnos}
    return render(request, 'alumnosDeCurso.html', data)