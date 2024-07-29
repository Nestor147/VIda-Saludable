from rest_framework import viewsets
from .models import Role, Usuario, Alimentacion, Agua, Esperanza, Sol, Aire, Sleep, Despertar, Ejercicio
from .serializers import (RoleSerializer, UsuarioSerializer, AlimentacionSerializer, AguaSerializer, 
                          EsperanzaSerializer, SolSerializer, AireSerializer, SleepSerializer, 
                          DespertarSerializer, EjercicioSerializer)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AlimentacionViewSet(viewsets.ModelViewSet):
    queryset = Alimentacion.objects.all()
    serializer_class = AlimentacionSerializer

class AguaViewSet(viewsets.ModelViewSet):
    queryset = Agua.objects.all()
    serializer_class = AguaSerializer

class EsperanzaViewSet(viewsets.ModelViewSet):
    queryset = Esperanza.objects.all()
    serializer_class = EsperanzaSerializer

class SolViewSet(viewsets.ModelViewSet):
    queryset = Sol.objects.all()
    serializer_class = SolSerializer

class AireViewSet(viewsets.ModelViewSet):
    queryset = Aire.objects.all()
    serializer_class = AireSerializer

class SleepViewSet(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

class DespertarViewSet(viewsets.ModelViewSet):
    queryset = Despertar.objects.all()
    serializer_class = DespertarSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
