# Generated by Django 4.1.2 on 2022-10-18 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_servicio_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='observacion',
            field=models.CharField(max_length=1000),
        ),
    ]
