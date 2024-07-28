from django.urls import path
from .views import (
    UsuarioListCreate, UsuarioDetail, AlimentacionListCreate, AlimentacionDetail,
    AguaListCreate, AguaDetail, EsperanzaListCreate, EsperanzaDetail,
    SolListCreate, SolDetail, AireListCreate, AireDetail, SleepListCreate, 
    SleepDetail, DespertarListCreate, DespertarDetail, EjercicioListCreate, EjercicioDetail
)

urlpatterns = [
    path('usuarios/', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),
    path('alimentacion/', AlimentacionListCreate.as_view(), name='alimentacion-list-create'),
    path('alimentacion/<int:pk>/', AlimentacionDetail.as_view(), name='alimentacion-detail'),
    path('agua/', AguaListCreate.as_view(), name='agua-list-create'),
    path('agua/<int:pk>/', AguaDetail.as_view(), name='agua-detail'),
    path('esperanza/', EsperanzaListCreate.as_view(), name='esperanza-list-create'),
    path('esperanza/<int:pk>/', EsperanzaDetail.as_view(), name='esperanza-detail'),
    path('sol/', SolListCreate.as_view(), name='sol-list-create'),
    path('sol/<int:pk>/', SolDetail.as_view(), name='sol-detail'),
    path('aire/', AireListCreate.as_view(), name='aire-list-create'),
    path('aire/<int:pk>/', AireDetail.as_view(), name='aire-detail'),
    path('sleep/', SleepListCreate.as_view(), name='sleep-list-create'),
    path('sleep/<int:pk>/', SleepDetail.as_view(), name='sleep-detail'),
    path('despertar/', DespertarListCreate.as_view(), name='despertar-list-create'),
    path('despertar/<int:pk>/', DespertarDetail.as_view(), name='despertar-detail'),
    path('ejercicio/', EjercicioListCreate.as_view(), name='ejercicio-list-create'),
    path('ejercicio/<int:pk>/', EjercicioDetail.as_view(), name='ejercicio-detail'),
]
