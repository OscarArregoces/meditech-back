# Generated by Django 4.1.2 on 2022-10-18 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_servicio_empleadoid_usuario_tipo_rolesid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
    ]
