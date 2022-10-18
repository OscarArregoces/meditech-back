from rest_framework import serializers
from .models import * 


class MaestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maestra
        fields = '__all__'
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'
class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'


# <---------///  PERSONALIZADAS  /// --------->

class CheckUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  
        fields = ('usuario','contraseña')

class ServiciosDetailSerializer(serializers.ModelSerializer):
    tipo_productoId= MaestraSerializer( read_only= True)
    usuarioId= UsuarioSerializer( read_only= True)
    class Meta:
        model = Servicio  
        fields = '__all__'

class UpdateServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio  
        fields = '__all__'
