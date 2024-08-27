from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Alimentacion, Agua, Esperanza, Sol, Aire, Dormir, Despertar, Ejercicio
from ..serializers import (AlimentacionSerializer, AguaSerializer, EsperanzaSerializer, 
                            SolSerializer, AireSerializer, DormirSerializer, DespertarSerializer, EjercicioSerializer)
from .analizadorhabitos import AnalizadorHabitosVida

class HabitosAPIView(APIView):
    def get(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        
        try:
            alimentacion = Alimentacion.objects.get(user_id=usuario_id)
            agua = Agua.objects.get(user_id=usuario_id)
            esperanza = Esperanza.objects.get(user_id=usuario_id)
            sol = Sol.objects.get(user_id=usuario_id)
            aire = Aire.objects.get(user_id=usuario_id)
            dormir = Dormir.objects.get(user_id=usuario_id)
            despertar = Despertar.objects.get(user_id=usuario_id)
            ejercicio = Ejercicio.objects.get(user_id=usuario_id)
        except (Alimentacion.DoesNotExist, Agua.DoesNotExist, Esperanza.DoesNotExist, Sol.DoesNotExist, 
                Aire.DoesNotExist, Dormir.DoesNotExist, Despertar.DoesNotExist, Ejercicio.DoesNotExist):
            return Response({"detail": "Datos del usuario no encontrados."}, status=status.HTTP_404_NOT_FOUND)
        
        # Análisis de cada hábito
        alimentacion_status = AnalizadorHabitosVida.clasificar_alimentacion(alimentacion.tipo_alimento, alimentacion.saludable)
        agua_status = AnalizadorHabitosVida.clasificar_consumo_agua(agua.cantidad)
        esperanza_status = AnalizadorHabitosVida.clasificar_esperanza(esperanza.tipo_practica)
        sol_status = AnalizadorHabitosVida.clasificar_sol(sol.tiempo)
        aire_status = AnalizadorHabitosVida.clasificar_aire(aire.tiempo)
        dormir_status = AnalizadorHabitosVida.clasificar_sueno(dormir.hora, despertar.hora)
        ejercicio_status = AnalizadorHabitosVida.clasificar_ejercicio(ejercicio.tipo, ejercicio.tiempo)
        
        return Response({
            'alimentacion': AlimentacionSerializer(alimentacion).data,
            'alimentacion_status': alimentacion_status,

            'agua': AguaSerializer(agua).data,
            'agua_status': agua_status,

            'esperanza': EsperanzaSerializer(esperanza).data,
            'esperanza_status': esperanza_status,

            'sol': SolSerializer(sol).data,
            'sol_status': sol_status,

            'aire': AireSerializer(aire).data,
            'aire_status': aire_status,

            'dormir': DormirSerializer(dormir).data,
            'dormir_status': dormir_status,

            'ejercicio': EjercicioSerializer(ejercicio).data,
            'ejercicio_status': ejercicio_status,
        })
