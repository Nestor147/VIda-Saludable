from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from ..models import DatosUsuario
from ..serializers import DatosUsuarioSerializer
from .analizadorsalud import AnalizadorSalud

class HealthIndicatorsComparisonAPIView(APIView):
    queryset = DatosUsuario.objects.all()
    serializer_class = DatosUsuarioSerializer

    def get(self, request, *args, **kwargs):
        usuario_id = self.kwargs.get('usuario_id')
        try:
            datos_iniciales = DatosUsuario.objects.get(user_id=usuario_id, tipo='inicial')
            datos_finales = DatosUsuario.objects.get(user_id=usuario_id, tipo='final')
        except DatosUsuario.DoesNotExist:
            return Response({"detail": "Datos del usuario no encontrados."}, status=status.HTTP_404_NOT_FOUND)

        # Realizar comparaciones entre los datos iniciales y finales
        analisis_comparativo = self.realizar_comparacion(datos_iniciales, datos_finales)

        return Response(analisis_comparativo)

    def realizar_comparacion(self, datos_iniciales, datos_finales):
        analisis = {}

        def convertir_a_float(valor):
            """Convierte un valor a float y maneja posibles errores."""
            try:
                return float(valor)
            except (ValueError, TypeError):
                return None  # O manejar el error de otra manera si no se puede convertir

        def calcular_mejora(inicial, final):
            """Calcula la diferencia entre el valor inicial y final."""
            inicial = convertir_a_float(inicial)
            final = convertir_a_float(final)
            if inicial is None or final is None:
                return None  # O manejar el error de otra manera
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

        def generar_advertencia(status_inicial, status_final, indicador):
            """Genera una advertencia si el indicador ha empeorado."""
            if status_inicial == 'No disponible' or status_final == 'No disponible':
                return f"Datos no disponibles para {indicador}."
            if status_final < status_inicial:
                return f"{indicador} ha empeorado, es recomendable que consultes a un médico."
            elif status_final == status_inicial:
                return f"{indicador} no ha mostrado cambios significativos."
            else:
                return f"{indicador} ha mejorado, sigue así."


     
        resultado_grasa_corporal=AnalizadorSalud.clasificar_grasa_corporal(datos_finales.imc, datos_finales.edad ,datos_finales.sexo )
            

    
        resultado_test_rufier=AnalizadorSalud.clasificar_resultado_test_rufier(datos_finales.frecuencia_cardiaca_en_reposo, datos_finales.frecuencia_cardiaca_despues_de_45_segundos , datos_finales.frecuencia_cardiaca_1_minuto_despues )
         



        # Lista de indicadores a comparar
        indicadores = [
            ('peso', datos_iniciales.peso, datos_finales.peso, AnalizadorSalud.clasificar_peso),
            ('altura', datos_iniciales.altura, datos_finales.altura, AnalizadorSalud.clasificar_altura),
            ('imc', datos_iniciales.imc ,datos_finales.imc , AnalizadorSalud.clasificar_imc),
            ('presion_sistolica', datos_iniciales.presion_sistolica, datos_finales.presion_sistolica, AnalizadorSalud.clasificar_presion_sistolica),
            ('presion_diastolica', datos_iniciales.presion_diastolica, datos_finales.presion_diastolica, AnalizadorSalud.clasificar_presion_diastolica),
            ('radio_abdominal', datos_iniciales.radio_abdominal, datos_finales.radio_abdominal,
                lambda x: AnalizadorSalud.clasificar_radio_abdominal(x, datos_iniciales.sexo)),    
            ('grasa_corporal',datos_iniciales.grasa_corporal , datos_finales.grasa_corporal ,lambda x: resultado_grasa_corporal),
            ('grasa_visceral', datos_iniciales.grasa_visceral, datos_finales.grasa_visceral, AnalizadorSalud.clasificar_grasa_visceral),
            ('frecuencia_cardiaca', datos_iniciales.frecuencia_cardiaca, datos_finales.frecuencia_cardiaca, AnalizadorSalud.clasificar_frecuencia_cardiaca),
            ('frecuencia_respiratoria', datos_iniciales.frecuencia_respiratoria, datos_finales.frecuencia_respiratoria, AnalizadorSalud.clasificar_frecuencia_respiratoria),
            ('colesterol_total', datos_iniciales.colesterol_total, datos_finales.colesterol_total, AnalizadorSalud.clasificar_colesterol_total),
            ('colesterol_hdl', datos_iniciales.colesterol_hdl, datos_finales.colesterol_hdl,
             lambda x: AnalizadorSalud.clasificar_colesterol_hdl(x, datos_iniciales.sexo)),
            ('colesterol_ldl', datos_iniciales.colesterol_ldl, datos_finales.colesterol_ldl, AnalizadorSalud.clasificar_colesterol_ldl),
            ('trigliceridos', datos_iniciales.trigliceridos, datos_finales.trigliceridos, AnalizadorSalud.clasificar_trigliceridos),
            ('glucosa', datos_iniciales.glucosa, datos_finales.glucosa, AnalizadorSalud.clasificar_glucosa),
            ('frecuencia_cardiaca_en_reposo', datos_iniciales.frecuencia_cardiaca_en_reposo, datos_finales.frecuencia_cardiaca_en_reposo, AnalizadorSalud.clasificar_frecuencia_cardiaca_reposo),
            ('frecuencia_cardiaca_despues_de_45_segundos', datos_iniciales.frecuencia_cardiaca_despues_de_45_segundos, datos_finales.frecuencia_cardiaca_despues_de_45_segundos, AnalizadorSalud.clasificar_frecuencia_cardiaca_45_segundos),
            ('frecuencia_cardiaca_1_minuto_despues', datos_iniciales.frecuencia_cardiaca_1_minuto_despues, datos_finales.frecuencia_cardiaca_1_minuto_despues, AnalizadorSalud.clasificar_frecuencia_cardiaca_1_minuto),
            ('resultado_test_rufier',datos_iniciales.resultado_test_rufier ,datos_finales.resultado_test_rufier,lambda x:resultado_test_rufier )
        ]


   
        umbral_mejora = Decimal(0.1)

        for indicador, valor_inicial, valor_final, clasificador in indicadores:
            mejora = calcular_mejora(valor_inicial, valor_final)
            status_inicial = clasificador(valor_inicial)
            status_final = clasificador(valor_final)

            analisis[indicador] = {
                'inicial': valor_inicial,
                'final': valor_final,
                'mejora': mejora,
                'diferencia': calcular_mejora(valor_inicial, valor_final),
                'status_inicial': status_inicial,
                'status_final': status_final,
                'recomendacion': generar_recomendacion(mejora, umbral_mejora, indicador),
                'advertencia': generar_advertencia(status_inicial, status_final, indicador)
            }

        return analisis
