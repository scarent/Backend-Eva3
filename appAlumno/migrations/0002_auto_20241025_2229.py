# Generated by Django 3.2 on 2024-10-26 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAlumno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='dni',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(),
        ),
    ]