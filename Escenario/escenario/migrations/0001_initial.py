# Generated by Django 3.2.22 on 2023-10-11 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField()),
                ('fecha_asignacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('duracion_estimada', models.FloatField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electrónico', models.CharField(blank=True, max_length=100, unique=True)),
                ('contraseña', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('prioridad', models.IntegerField()),
                ('estadio', models.CharField(choices=[('PE', 'Pendiente'), ('PR', 'Progreso'), ('CO', 'Completada')], max_length=2)),
                ('completada', models.BooleanField()),
                ('fecha_creacion', models.DateField()),
                ('hora_vencimiento', models.TimeField()),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador2', to='escenario.usuario')),
                ('usuario', models.ManyToManyField(related_name='usuario2', through='escenario.AsignacionTarea', to='escenario.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoAsignado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.proyecto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador', to='escenario.usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tareas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.tarea'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='usuarios',
            field=models.ManyToManyField(related_name='usuarios', through='escenario.ProyectoAsignado', to='escenario.Usuario'),
        ),
        migrations.CreateModel(
            name='EtiquetaAsociada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.etiqueta')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.tarea')),
            ],
        ),
        migrations.AddField(
            model_name='etiqueta',
            name='tareas',
            field=models.ManyToManyField(through='escenario.EtiquetaAsociada', to='escenario.Tarea'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_comentario', models.DateTimeField()),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='escenario.usuario')),
                ('tarea', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='escenario.tarea')),
            ],
        ),
        migrations.AddField(
            model_name='asignaciontarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.tarea'),
        ),
        migrations.AddField(
            model_name='asignaciontarea',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escenario.usuario'),
        ),
    ]
