from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from ..models import DatosCorporales, DatosHabitos, Usuario
from ..serializers import DatosCorporalesSerializer, DatosHabitosSerializer
from .analizadorsalud import AnalizadorSalud

class HealthIndicatorsComparisonAPIView(APIView):
    queryset = Usuario.objects.all()
    serializer_class = DatosCorporalesSerializer

    def get(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        try:
            # Obtén datos corporales iniciales y finales
            datos_iniciales_corporales = DatosCorporales.objects.get(usuario_id=usuario_id, tipo='inicial')
            datos_finales_corporales = DatosCorporales.objects.get(usuario_id=usuario_id, tipo='final')
            
            # Obtén datos de hábitos iniciales y finales
            datos_iniciales_habitos = DatosHabitos.objects.get(usuario_id=usuario_id, tipo='inicial')
            datos_finales_habitos = DatosHabitos.objects.get(usuario_id=usuario_id, tipo='final')

        except (DatosCorporales.DoesNotExist, DatosHabitos.DoesNotExist):
            return Response({"detail": "Datos del usuario no encontrados."}, status=status.HTTP_404_NOT_FOUND)

        # Realizar comparaciones entre los datos iniciales y finales
        analisis_comparativo = self.realizar_comparacion(datos_iniciales_corporales, datos_finales_corporales, datos_iniciales_habitos, datos_finales_habitos)

        return Response(analisis_comparativo)

    def realizar_comparacion(self, datos_iniciales_corporales, datos_finales_corporales, datos_iniciales_habitos, datos_finales_habitos):
        analisis = {}

        def convertir_a_float(valor):
            """Convierte un valor a float y maneja posibles errores."""
            try:
                return float(valor)
            except (ValueError, TypeError):
                return None

        def calcular_mejora(inicial, final):
            """Calcula la diferencia entre el valor inicial y final."""
            inicial = convertir_a_float(inicial)
            final = convertir_a_float(final)
            if inicial is None or final is None:
                return None
            return final - inicial

        def generar_recomendacion(mejora, umbral_mejora, indicador):
            """Genera una recomendación basada en la mejora o deterioro del indicador."""
            if mejora is None:
                return f"Datos no válidos para {indicador}."
            if mejora < 0:
                return f"Se ha logrado una mejora en {indicador}. ¡Continúa con el buen trabajo!"
            elif mejora > umbral_mejora:
                return f"Es necesario mejorar en {indicador}. Considera cambios en tu estilo de vida."
            else:
                return f"El {indicador} se mantiene estable. Continúa monitoreando."

        # Lista de indicadores corporales
        indicadores_corporales = [
            ('peso', datos_iniciales_corporales.peso, datos_finales_corporales.peso, AnalizadorSalud.clasificar_peso),
            ('altura', datos_iniciales_corporales.altura, datos_finales_corporales.altura, AnalizadorSalud.clasificar_altura),
            ('imc', datos_iniciales_corporales.imc, datos_finales_corporales.imc, AnalizadorSalud.clasificar_imc),
            ('presion_sistolica', datos_iniciales_corporales.presion_sistolica, datos_finales_corporales.presion_sistolica, AnalizadorSalud.clasificar_presion_sistolica),
            ('presion_diastolica', datos_iniciales_corporales.presion_diastolica, datos_finales_corporales.presion_diastolica, AnalizadorSalud.clasificar_presion_diastolica),
            # Añadir más indicadores corporales aquí
        ]

        # Lista de indicadores de hábitos
        indicadores_habitos = [
            ('consumo_3_comidas_horario_fijo', datos_iniciales_habitos.consumo_3_comidas_horario_fijo, datos_finales_habitos.consumo_3_comidas_horario_fijo),
            ('consumo_5_porciones_frutas_verduras', datos_iniciales_habitos.consumo_5_porciones_frutas_verduras, datos_finales_habitos.consumo_5_porciones_frutas_verduras),
            ('consumo_3_porciones_proteinas', datos_iniciales_habitos.consumo_3_porciones_proteinas, datos_finales_habitos.consumo_3_porciones_proteinas),
            ('bebo_8_vasos_agua', datos_iniciales_habitos.bebo_8_vasos_agua, datos_finales_habitos.bebo_8_vasos_agua),
            # Añadir más indicadores de hábitos aquí
        ]

        # Comparación de indicadores corporales
        for indicador, inicial, final, clasificador in indicadores_corporales:
            mejora = calcular_mejora(inicial, final)
            clasificacion_inicial = clasificador(inicial) if inicial is not None else "No disponible"
            clasificacion_final = clasificador(final) if final is not None else "No disponible"
            analisis[indicador] = {
                'inicial': inicial,
                'final': final,
                'mejora': mejora,
                'clasificacion_inicial': clasificacion_inicial,
                'clasificacion_final': clasificacion_final,
                'recomendacion': generar_recomendacion(mejora, umbral_mejora=0.5, indicador=indicador)
            }

        # Comparación de hábitos
        for indicador, inicial, final in indicadores_habitos:
            mejora = calcular_mejora(inicial, final)
            analisis[indicador] = {
                'inicial': inicial,
                'final': final,
                'mejora': mejora,
                'recomendacion': generar_recomendacion(mejora, umbral_mejora=0.5, indicador=indicador)
            }

        return analisis
