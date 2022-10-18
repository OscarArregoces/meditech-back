from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Maestra (models.Model):
    nombre_1 = models.CharField(max_length=30)
    nombre_2 = models.CharField(max_length=30, null= True, blank=True)
    dependencia = models.IntegerField(null= True, blank=True)
    estado = models.IntegerField(null= True, blank=True)

class Persona (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    numero_documento = models.CharField(max_length=30)
    tipo_identificacion = models.ForeignKey(Maestra, related_name= 'tipo_identificacion', on_delete=models.CASCADE)
    tipo_sexo = models.ForeignKey(Maestra, related_name= 'tipo_sexo', on_delete=models.CASCADE)

class Usuario (models.Model):
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    personaId = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_estadoId = models.ForeignKey(Maestra, related_name= 'tipo_estadoId', on_delete=models.CASCADE)
    tipo_rolesId = models.ForeignKey(Maestra,related_name= 'tipo_rolesId', on_delete=models.CASCADE)

class Servicio (models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    fecha_ingreso = models.DateField()
    usuarioId = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    tipo_productoId = models.ForeignKey(Maestra,related_name= 'tipo_producto', on_delete=models.CASCADE)
    empleadoId = models.ForeignKey(Usuario,related_name= 'empleadoId', on_delete=models.CASCADE, blank= True, null=True)

    
class Respuesta (models.Model):
    observacion = models.CharField(max_length=1000)
    fecha_salida = models.DateField()
    servicioId = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    tipo_estado = models.ForeignKey(Maestra,related_name= 'tipo_estado', on_delete=models.CASCADE)