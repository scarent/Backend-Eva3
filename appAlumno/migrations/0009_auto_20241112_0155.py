# Generated by Django 3.2 on 2024-11-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAlumno', '0008_merge_20241112_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(default='Desconocido', max_length=30),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='cursos',
            field=models.ManyToManyField(related_name='alumnos', to='appAlumno.Curso'),
        ),
    ]