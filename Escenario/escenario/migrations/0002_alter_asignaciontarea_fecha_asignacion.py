# Generated by Django 3.2.22 on 2023-10-11 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('escenario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignaciontarea',
            name='fecha_asignacion',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]