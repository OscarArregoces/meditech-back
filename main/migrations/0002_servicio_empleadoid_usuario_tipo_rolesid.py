# Generated by Django 4.1.2 on 2022-10-18 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='empleadoId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleadoId', to='main.usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_rolesId',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_rolesId', to='main.maestra'),
            preserve_default=False,
        ),
    ]
