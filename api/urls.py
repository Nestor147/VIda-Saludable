from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (RoleViewSet, UsuarioViewSet, AlimentacionViewSet, AguaViewSet, EsperanzaViewSet, 
                    SolViewSet, AireViewSet, SleepViewSet, DespertarViewSet, EjercicioViewSet)

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'alimentaciones', AlimentacionViewSet)
router.register(r'aguas', AguaViewSet)
router.register(r'esperanzas', EsperanzaViewSet)
router.register(r'soles', SolViewSet)
router.register(r'aires', AireViewSet)
router.register(r'sleeps', SleepViewSet)
router.register(r'despertares', DespertarViewSet)
router.register(r'ejercicios', EjercicioViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
urlpatterns =router.urls
