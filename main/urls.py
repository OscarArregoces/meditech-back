from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('maestra',  MaestraViewSet)
router.register('persona',  PersonaViewSet)
router.register('usuario',  UsuarioViewSet)
router.register('respuesta',  RespuestaViewSet)
router.register('servicio',  ServicioViewSet)

urlpatterns = router.urls