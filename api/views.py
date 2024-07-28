from rest_framework import generics
from .models import Usuario, Alimentacion, Agua, Esperanza, Sol, Aire, Sleep, Despertar, Ejercicio
from .serializers import (
    UsuarioSerializer, AlimentacionSerializer, AguaSerializer, EsperanzaSerializer,
    SolSerializer, AireSerializer, SleepSerializer, DespertarSerializer, EjercicioSerializer
)

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AlimentacionListCreate(generics.ListCreateAPIView):
    queryset = Alimentacion.objects.all()
    serializer_class = AlimentacionSerializer

class AlimentacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alimentacion.objects.all()
    serializer_class = AlimentacionSerializer

class AguaListCreate(generics.ListCreateAPIView):
    queryset = Agua.objects.all()
    serializer_class = AguaSerializer

class AguaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agua.objects.all()
    serializer_class = AguaSerializer

class EsperanzaListCreate(generics.ListCreateAPIView):
    queryset = Esperanza.objects.all()
    serializer_class = EsperanzaSerializer

class EsperanzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Esperanza.objects.all()
    serializer_class = EsperanzaSerializer

class SolListCreate(generics.ListCreateAPIView):
    queryset = Sol.objects.all()
    serializer_class = SolSerializer

class SolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sol.objects.all()
    serializer_class = SolSerializer

class AireListCreate(generics.ListCreateAPIView):
    queryset = Aire.objects.all()
    serializer_class = AireSerializer

class AireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aire.objects.all()
    serializer_class = AireSerializer

class SleepListCreate(generics.ListCreateAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

class SleepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

class DespertarListCreate(generics.ListCreateAPIView):
    queryset = Despertar.objects.all()
    serializer_class = DespertarSerializer

class DespertarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despertar.objects.all()
    serializer_class = DespertarSerializer

class EjercicioListCreate(generics.ListCreateAPIView):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class EjercicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
