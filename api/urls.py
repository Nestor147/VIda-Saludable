from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet, UsuarioViewSet, AlimentacionViewSet, AguaViewSet, EsperanzaViewSet, 
    SolViewSet, AireViewSet, DormirViewSet, DespertarViewSet, EjercicioViewSet, ProyectoViewSet, UsuarioProyectoViewSet, DatosUsuarioViewSet
)
from .health.viewindicator import HealthIndicatorsAPIView
from .health.viewindicatorproject import IndicadoresSaludPorProyectoView

from .habits.viewhabitsbyuser import HabitosAPIView


router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'alimentaciones', AlimentacionViewSet)
router.register(r'aguas', AguaViewSet)
router.register(r'esperanzas', EsperanzaViewSet)
router.register(r'soles', SolViewSet)
router.register(r'aires', AireViewSet)
router.register(r'sleeps', DormirViewSet)
router.register(r'despertares', DespertarViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'usuario-proyectos', UsuarioProyectoViewSet)
router.register(r'datos-iniciales', DatosUsuarioViewSet)

urlpatterns = [
    path('indicadores-salud-pr-usuario/<int:usuario_id>/', HealthIndicatorsAPIView.as_view(), name='indicadores_salud'),
    path('indicadores-salud-por-proyectos/<int:proyecto_id>/', IndicadoresSaludPorProyectoView.as_view(), name='proyecto-detalle'),
    path('indicadores-habitos-por-usuario/<int:usuario_id>/', HabitosAPIView.as_view(), name='indicador-de-habito'),

]

urlpatterns += router.urls
