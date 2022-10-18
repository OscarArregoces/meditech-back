from msilib.schema import Class
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db.models import Q
import json


class MaestraViewSet(viewsets.ModelViewSet):
    queryset = Maestra.objects.all()
    serializer_class = MaestraSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


# <---------///  PERSONALIZADAS  /// --------->

class CheckUsuario(APIView):
    queryset = Usuario.objects.all()
    serializer_class = CheckUsuarioSerializer

    def post(self, request, *args, **kwargs):
        usuario = request.data['usuario']
        contraseña = request.data['contraseña']
        userExist = Usuario.objects.filter(
            Q(usuario=usuario) & Q(contraseña=contraseña))[0]
        if (userExist):
            userVerificated = CheckUsuarioSerializer(data= {'usuario': userExist.usuario , 'contraseña': userExist.contraseña})
            if( userVerificated.is_valid() ):
                datosPersona = Persona.objects.get( pk=userExist.personaId_id)
                print(datosPersona.tipo_identificacion.pk)
                data = {
                    'id' : userExist.id,
                    'usuario' : userExist.usuario,
                    'empresa' : userExist.empresa,
                    'tipo_rolesId': userExist.tipo_rolesId_id,
                    'persona' : {
                        'id': userExist.personaId_id,
                        'nombre': datosPersona.nombre,
                        'apellido': datosPersona.apellido,
                        'nacionalidad': datosPersona.nacionalidad,
                        'email': datosPersona.email,
                        'telefono': datosPersona.telefono,
                        'numero_documento': datosPersona.numero_documento,
                        'tipo_identificacion_id': datosPersona.tipo_identificacion.nombre_1,
                        'tipo_sexo': datosPersona.tipo_sexo.nombre_1,
                    }
                }
                return HttpResponse(json.dumps({'ok': True, 'data':data}))
            else:
                return HttpResponse({'ok': False, 'msg':' Error interno, usuario no valido'})
        else:
            return HttpResponse({'ok': False, 'msg': 'El usuario no existe en la DB'})

class ServiciosDetail(APIView):
    queryset = Servicio.objects.all()
    serializer_class = ServiciosDetailSerializer

    def get(self, request, *args, **kwargs):

        servicio = Servicio.objects.all()
        servicioValid = ServiciosDetailSerializer(servicio, many=True)

        return Response(servicioValid.data)


class UpdateServicio(UpdateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = UpdateServicioSerializer

    def put(self, request, *args, **kwargs):
        print(request.data)
        return super().put(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):

    #     newServicio = request.data
    #     servicioValid = ServiciosDetailSerializer(data=newServicio)

    #     if(servicioValid.is_valid()):
    #         servicioValid.save()
    #         return Response(servicioValid.data)
    #     else:
    #         return Response(servicioValid.errors)
        
        # todo_instance = self.get_object(todo_id, request.user.id)
        # data = {
        #     'task': request.data.get('task'), 
        #     'completed': request.data.get('completed'), 
        #     'user': request.user.id
        # }
        # serializer = TodoSerializer(instance = todo_instance, data=data, partial = True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

