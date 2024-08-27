from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from ..models import Proyecto, UsuarioProyecto, DatosUsuario
from ..serializers import DatosUsuarioSerializer
from decimal import Decimal
from .analizadorsalud import AnalizadorSalud

class IndicadoresSaludPorProyectoView(APIView):

    def get(self, request, proyecto_id, *args, **kwargs):
        # Verificar si el proyecto existe
        if not Proyecto.objects.filter(id=proyecto_id).exists():
            return Response({"detail": "El proyecto no existe."}, status=status.HTTP_404_NOT_FOUND)

        # Obtener los usuarios asociados al proyecto
        usuario_proyectos = UsuarioProyecto.objects.filter(proyecto_id=proyecto_id)
        usuarios_ids = usuario_proyectos.values_list('usuario_id', flat=True)

        if not usuarios_ids:
            return Response({"detail": "No se encontraron usuarios para este proyecto."}, status=status.HTTP_404_NOT_FOUND)

        # Obtener los datos de salud de los usuarios asociados al proyecto
        datos = DatosUsuario.objects.filter(user_id__in=usuarios_ids, tipo='inicial')

        if not datos.exists():
            return Response({"detail": "No se encontraron datos de salud para los usuarios del proyecto."}, status=status.HTTP_404_NOT_FOUND)

        # Calcular el promedio de cada indicador
        promedios = datos.aggregate(
            promedio_peso=Avg('peso'),
            promedio_altura=Avg('altura'),
            promedio_presion_sistolica=Avg('presion_sistolica'),
            promedio_presion_diastolica=Avg('presion_diastolica'),
            promedio_radio_abdominal=Avg('radio_abdominal'),
            promedio_grasa_corporal=Avg('grasa_corporal'),
            promedio_grasa_visceral=Avg('grasa_visceral'),
            promedio_frecuencia_cardiaca=Avg('frecuencia_cardiaca'),
            promedio_frecuencia_respiratoria=Avg('frecuencia_respiratoria'),
            promedio_colesterol_total=Avg('colesterol_total'),
            promedio_colesterol_hdl=Avg('colesterol_hdl'),
            promedio_colesterol_ldl=Avg('colesterol_ldl'),
            promedio_trigliceridos=Avg('trigliceridos'),
            promedio_glucosa=Avg('glucosa'),
            promedio_frecuencia_cardiaca_en_reposo=Avg('frecuencia_cardiaca_en_reposo'),
            promedio_frecuencia_cardiaca_despues_de_45_segundos=Avg('frecuencia_cardiaca_despues_de_45_segundos'),
            promedio_frecuencia_cardiaca_1_minuto_despues=Avg('frecuencia_cardiaca_1_minuto_despues'),
            promedio_resultado_test_rufier=Avg('resultado_test_rufier'),
            promedio_resultado_edades=Avg('edad')
        )

        # Acceder a los valores de 'promedios'
        promedio_peso = promedios['promedio_peso']
        promedio_altura = promedios['promedio_altura']
        promedio_presion_sistolica = promedios['promedio_presion_sistolica']
        promedio_presion_diastolica = promedios['promedio_presion_diastolica']
        promedio_radio_abdominal = promedios['promedio_radio_abdominal']
        promedio_grasa_corporal = promedios['promedio_grasa_corporal']
        promedio_grasa_visceral = promedios['promedio_grasa_visceral']
        promedio_frecuencia_cardiaca = promedios['promedio_frecuencia_cardiaca']
        promedio_frecuencia_respiratoria = promedios['promedio_frecuencia_respiratoria']
        promedio_colesterol_total = promedios['promedio_colesterol_total']
        promedio_colesterol_hdl = promedios['promedio_colesterol_hdl']
        promedio_colesterol_ldl = promedios['promedio_colesterol_ldl']
        promedio_trigliceridos = promedios['promedio_trigliceridos']
        promedio_glucosa = promedios['promedio_glucosa']
        promedio_frecuencia_cardiaca_en_reposo = promedios['promedio_frecuencia_cardiaca_en_reposo']
        promedio_frecuencia_cardiaca_despues_de_45_segundos = promedios['promedio_frecuencia_cardiaca_despues_de_45_segundos']
        promedio_frecuencia_cardiaca_1_minuto_despues = promedios['promedio_frecuencia_cardiaca_1_minuto_despues']
        promedio_resultado_test_rufier = promedios['promedio_resultado_test_rufier']
        promedio_resultado_edades = promedios['promedio_resultado_edades']

        # 1. Peso
        peso_status = AnalizadorSalud.clasificar_peso(promedio_peso)

        # 2. Altura
        altura_status = AnalizadorSalud.clasificar_altura(promedio_altura)

        # 3. IMC
        imc = AnalizadorSalud.calcular_imc(promedio_peso, promedio_altura)
        imc_status = AnalizadorSalud.clasificar_imc(imc)

        # 4. Presión Arterial Sistólica
        sistolica_status = AnalizadorSalud.clasificar_presion_sistolica(promedio_presion_sistolica)

        # 5. Presión Arterial Diastólica
        diastolica_status = AnalizadorSalud.clasificar_presion_diastolica(promedio_presion_diastolica)

        # 6. Radio Abdominal
        radio_abdominal_status_M = AnalizadorSalud.clasificar_radio_abdominal(promedio_radio_abdominal, 'M')
        radio_abdominal_status_F = AnalizadorSalud.clasificar_radio_abdominal(promedio_radio_abdominal, 'F')

        # 7. Grasa Corporal (%)
        grasa_corporal_status_M = AnalizadorSalud.clasificar_grasa_corporal(imc, promedio_resultado_edades, 'M')
        grasa_corporal_status_F = AnalizadorSalud.clasificar_grasa_corporal(imc, promedio_resultado_edades, 'F')

        # 8. Grasa Visceral
        grasa_visceral_status = AnalizadorSalud.clasificar_grasa_visceral(promedio_grasa_visceral)

        # 9. Frecuencia Cardíaca
        frecuencia_cardiaca_status = AnalizadorSalud.clasificar_frecuencia_cardiaca(promedio_frecuencia_cardiaca)

        # 10. Frecuencia Respiratoria
        frecuencia_respiratoria_status = AnalizadorSalud.clasificar_frecuencia_respiratoria(promedio_frecuencia_respiratoria)

        # 11. Colesterol Total
        colesterol_total_status = AnalizadorSalud.clasificar_colesterol_total(promedio_colesterol_total)

        # 12. Colesterol HDL
        hdl_status_M = AnalizadorSalud.clasificar_colesterol_hdl(promedio_colesterol_hdl, 'M')
        hdl_status_F = AnalizadorSalud.clasificar_colesterol_hdl(promedio_colesterol_hdl, 'F')

        # 13. Colesterol LDL
        ldl_status = AnalizadorSalud.clasificar_colesterol_ldl(promedio_colesterol_ldl)

        # 14. Triglicéridos
        trigliceridos_status = AnalizadorSalud.clasificar_trigliceridos(promedio_trigliceridos)

        # 15. Glucosa
        glucosa_status = AnalizadorSalud.clasificar_glucosa(promedio_glucosa)

        # 16. Frecuencia Cardíaca en Reposo
        frecuencia_cardiaca_reposo_status = AnalizadorSalud.clasificar_frecuencia_cardiaca_reposo(promedio_frecuencia_cardiaca_en_reposo)

        # 17. Frecuencia Cardíaca Después de 45 Segundos
        frecuencia_cardiaca_45_seg_status = AnalizadorSalud.clasificar_frecuencia_cardiaca_45_segundos(promedio_frecuencia_cardiaca_despues_de_45_segundos)

        # 18. Frecuencia Cardíaca 1 Minuto Después
        frecuencia_cardiaca_1_min_status = AnalizadorSalud.clasificar_frecuencia_cardiaca_1_minuto(promedio_frecuencia_cardiaca_1_minuto_despues)

        # 19. Frecuencia Cardíaca 5 Minutos Después
        # Suponiendo que tienes los campos necesarios en tu modelo DatosUsuario
        frecuencia_cardiaca_5_minutos_despues_status = AnalizadorSalud.clasificar_resultado_test_rufier(
            promedio_frecuencia_cardiaca_en_reposo, promedio_frecuencia_cardiaca_despues_de_45_segundos, promedio_frecuencia_cardiaca_1_minuto_despues)

        return Response({
            "peso": {"promedio": promedio_peso, "status": peso_status},
            "altura": {"promedio": promedio_altura, "status": altura_status},
            "imc": {"valor": imc, "status": imc_status},
            "presion_sistolica": {"promedio": promedio_presion_sistolica, "status": sistolica_status},
            "presion_diastolica": {"promedio": promedio_presion_diastolica, "status": diastolica_status},
            "radio_abdominal": {"promedio": promedio_radio_abdominal, "status_M": radio_abdominal_status_M, "status_F": radio_abdominal_status_F},
            "grasa_corporal": {"promedio": promedio_grasa_corporal, "status_M": grasa_corporal_status_M, "status_F": grasa_corporal_status_F},
            "grasa_visceral": {"promedio": promedio_grasa_visceral, "status": grasa_visceral_status},
            "frecuencia_cardiaca": {"promedio": promedio_frecuencia_cardiaca, "status": frecuencia_cardiaca_status},
            "frecuencia_respiratoria": {"promedio": promedio_frecuencia_respiratoria, "status": frecuencia_respiratoria_status},
            "colesterol_total": {"promedio": promedio_colesterol_total, "status": colesterol_total_status},
            "colesterol_hdl": {"promedio": promedio_colesterol_hdl, "status_M": hdl_status_M, "status_F": hdl_status_F},
            "colesterol_ldl": {"promedio": promedio_colesterol_ldl, "status": ldl_status},
            "trigliceridos": {"promedio": promedio_trigliceridos, "status": trigliceridos_status},
            "glucosa": {"promedio": promedio_glucosa, "status": glucosa_status},
            "frecuencia_cardiaca_en_reposo": {"promedio": promedio_frecuencia_cardiaca_en_reposo, "status": frecuencia_cardiaca_reposo_status},
            "frecuencia_cardiaca_45_segundos": {"promedio": promedio_frecuencia_cardiaca_despues_de_45_segundos, "status": frecuencia_cardiaca_45_seg_status},
            "frecuencia_cardiaca_1_minuto": {"promedio": promedio_frecuencia_cardiaca_1_minuto_despues, "status": frecuencia_cardiaca_1_min_status},
            "resultado_test_rufier": {"promedio": promedio_resultado_test_rufier, "status": frecuencia_cardiaca_5_minutos_despues_status},
        }, status=status.HTTP_200_OK)



#region Basic Operations

 #endregion