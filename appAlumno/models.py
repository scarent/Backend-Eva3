from django.db import models
from appProfesor.models import Profesor
from django.core.exceptions import ValidationError


class Alumno(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=30, default="Desconocido")
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()
    # Relación con curso a través de la tabla intermedia Matricula
    cursos = models.ManyToManyField("Curso", through='Matricula') 

    def datos_alumno(self):
        return "{}, {}".format(self.nombre, self.dni)

    def __str__(self):
        return self.datos_alumno()


class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    horas = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()  # antes programa
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    seccion = models.CharField(max_length=20)  # antes numero
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser después de la fecha de termino.")

    def datos_curso(self):
        return "{}, {}".format(self.nombre, self.codigo)

    def __str__(self):
        return self.datos_curso()


class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} matriculado en {self.curso} el {self.fecha_matricula}"
