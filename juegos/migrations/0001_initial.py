# Generated by Django 5.1.2 on 2024-10-15 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_lanzamiento', models.DateField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.genero')),
            ],
        ),
    ]
