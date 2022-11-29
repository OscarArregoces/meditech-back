from msilib.schema import Class
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
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
            userVerificated = CheckUsuarioSerializer(
                data={'usuario': userExist.usuario, 'contraseña': userExist.contraseña})
            if (userVerificated.is_valid()):
                datosPersona = Persona.objects.get(pk=userExist.personaId_id)
                print(datosPersona.tipo_identificacion.pk)
                data = {
                    'id': userExist.id,
                    'usuario': userExist.usuario,
                    'empresa': userExist.empresa,
                    'tipo_rolesId': userExist.tipo_rolesId_id,
                    'persona': {
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
                return HttpResponse(json.dumps({'ok': True, 'data': data}))
            else:
                return HttpResponse({'ok': False, 'msg': ' Error interno, usuario no valido'})
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


# <---------///  CONSULTAS  /// --------->


class Consulta1(APIView):  # <---------///  CLASIFICACION DE SERVICIOS  /// --------->

    def get(self, request, *args, **kwargs):

        serviciosTotales = Servicio.objects.all()
        computadores = Servicio.objects.filter(tipo_productoId=13)
        monitores = Servicio.objects.filter(tipo_productoId=14)
        televisores = Servicio.objects.filter(tipo_productoId=15)
        video_beams = Servicio.objects.filter(tipo_productoId=16)

        response = {
            "servicios_totales": len(serviciosTotales),
            "data": [
                {
                    "titulo": "Computadores",
                    "cantidad": len(computadores),
                    "data": ServicioSerializer(computadores, many=True).data
                },
                {
                    "titulo": "Monitores",
                    "cantidad": len(monitores),
                    "data": ServicioSerializer(monitores, many=True).data
                },
                {
                    "titulo": "Televisores",
                    "cantidad": len(televisores),
                    "data": ServicioSerializer(televisores, many=True).data
                },
                {
                    "titulo": "Video Beams",
                    "cantidad": len(video_beams),
                    "data": ServicioSerializer(video_beams, many=True).data
                },
            ],
        }

        return JsonResponse(response, safe=False)
        # return HttpResponse(response, content_type='application/json')


class Consulta2(APIView):    # <---------///  CLASIFICACION DE CLIENTES  /// --------->

    def get(self, request, *args, **kwargs):

        clientes = Persona.objects.all().values()
        mujeres = Persona.objects.filter(tipo_sexo=10).values()
        hombres = Persona.objects.filter(tipo_sexo=11).values()

        response = {
            "clientes_totales": len(clientes),
            "data": [
                {
                    "titulo": "Clientes mujeres",
                    "cantidad": len(mujeres),
                    "data": list(mujeres),
                },
                {
                    "titulo": "Clientes hombres",
                    "cantidad": len(hombres),
                    "data": list(hombres),
                }
            ]
        }

        return JsonResponse(response, safe=False)


# <---------///  TODOS LOS SERVICIOS REALIZADOS EN UNA FECHA ESPECIFICA  /// --------->
class Consulta3(APIView):

    def post(self, request, *args, **kwargs):

        fecha1 = request.data['fecha1']
        servicios = Servicio.objects.filter(fecha_ingreso=fecha1)

        response = {
            "cantidad": len(servicios),
            "data": ServicioSerializer(servicios, many= True).data
        }

        return JsonResponse(response, safe=False)


# <---------///  TODOS LOS SERVICIOS REALIZADOS COMPRENDIDOS ENTRE DOS FECHAS  /// --------->
class Consulta4(APIView):

    def post(self, request, *args, **kwargs):

        fecha1 = request.data['fecha1']
        fecha2 = request.data['fecha2']

        servicios = Servicio.objects.filter(
            fecha_ingreso__range=[fecha1, fecha2])

        response = {
            "cantidad": len(servicios),
            "data": ServicioSerializer(servicios, many=True).data
        }

        return JsonResponse(response, safe=False)


class Consulta5(APIView):    # <---------///  REPORTE GENERAL  /// --------->

    def get(self, request, *args, **kwargs):

        # <---------///  1  /// --------->
        computadores = Servicio.objects.filter(tipo_productoId=13).values()
        monitores = Servicio.objects.filter(tipo_productoId=14).values()
        televisores = Servicio.objects.filter(tipo_productoId=15).values()
        video_beams = Servicio.objects.filter(tipo_productoId=16).values()

        # <---------///  2  /// --------->

        clientes = Persona.objects.all().values()
        mujeres = Persona.objects.filter(tipo_sexo=10).values()
        hombres = Persona.objects.filter(tipo_sexo=11).values()

        response = {
            "consulta1": {
                "computadores": {
                    "cantidad": len(computadores),
                    "data": list(computadores)
                },
                "monitores": {
                    "cantidad": len(monitores),
                    "data": list(monitores)
                },
                "televisores": {
                    "cantidad": len(televisores),
                    "data": list(televisores)
                },
                "video_beams": {
                    "cantidad": len(video_beams),
                    "data": list(video_beams)
                },
            },
            "consulta2": {
                "clientes_totales": len(clientes),
                "clientes_mujeres": list(mujeres),
                "clientes_hombres": list(hombres)
            },
        }

        return JsonResponse(response, safe=False)
