# Generated by Django 3.2 on 2024-10-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('edad', models.CharField(max_length=2)),
            ],
        ),
    ]