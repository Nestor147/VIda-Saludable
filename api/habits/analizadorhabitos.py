from decimal import Decimal
from datetime import datetime, timedelta


class AnalizadorHabitosVida:
    
    @staticmethod
    def clasificar_alimentacion(tipo_alimento, saludable):
        """
        Clasifica la calidad de la alimentación en función del tipo de alimento y si es saludable.
        """
        puntaje = 0

        if saludable.lower() == 'si':
            if tipo_alimento.lower() == 'desayuno':
                puntaje = 90
            elif tipo_alimento.lower() == 'almuerzo':
                puntaje = 100
            elif tipo_alimento.lower() == 'cena':
                puntaje = 80
            else:
                puntaje = 70
        else:
            puntaje = 50

        return puntaje


    @staticmethod
    def clasificar_consumo_agua(cantidad):
        """
        Clasifica el consumo de agua en función de la cantidad ingerida en mililitros.
        """
        if cantidad >= 2000:
            return 100
        elif 1500 <= cantidad < 2000:
            return 80
        elif 1000 <= cantidad < 1500:
            return 60
        else:
            return 40


    @staticmethod
    def clasificar_esperanza(tipo_practica):
        """
        Clasifica la práctica espiritual según el tipo de actividad realizada.
        """
        if tipo_practica.lower() == 'oracion':
            return 90
        elif tipo_practica.lower() == 'leer la biblia':
            return 100
        else:
            return 50


    @staticmethod
    def clasificar_sol(tiempo):
        """
        Clasifica la exposición al sol en función del tiempo en minutos.
        """
        if 15 <= tiempo <= 30:
            return 100
        elif 5 <= tiempo < 15 or 30 < tiempo <= 45:
            return 80
        else:
            return 50


    @staticmethod
    def clasificar_aire(tiempo):
        """
        Clasifica la exposición al aire fresco en función del tiempo en minutos.
        """
        if 20 <= tiempo <= 60:
            return 100
        elif 10 <= tiempo < 20 or 60 < tiempo <= 90:
            return 80
        else:
            return 50


    @staticmethod
    def clasificar_sueno(dormir_hora, despertar_hora):
        """
        Clasifica la calidad del sueño basándose en la cantidad de horas dormidas.
        """
        # Convierte los objetos time a datetime para poder restarlos
        hoy = datetime.now().date()  # Usa la fecha de hoy
        dormir_datetime = datetime.combine(hoy, dormir_hora)
        despertar_datetime = datetime.combine(hoy, despertar_hora)
        
        # Si la hora de despertar es menor que la hora de dormir, asumimos que despertó al día siguiente
        if despertar_datetime < dormir_datetime:
            despertar_datetime += timedelta(days=1)
        
        horas_dormidas = (despertar_datetime - dormir_datetime).seconds / 3600

        if 7 <= horas_dormidas <= 8:
            return 100
        elif 5 <= horas_dormidas < 7 or 8 < horas_dormidas <= 9:
            return 80
        else:
            return 60


    @staticmethod
    def clasificar_ejercicio(tipo, tiempo):
        """
        Clasifica el ejercicio en función del tipo y del tiempo en minutos.
        """
        if tipo.lower() == 'caminata lenta':
            return min(tiempo * 2, 100)
        elif tipo.lower() == 'caminata rapida':
            return min(tiempo * 2.5, 100)
        elif tipo.lower() == 'carrera':
            return min(tiempo * 3, 100)
        elif tipo.lower() == 'ejercicio guiado':
            return min(tiempo * 2, 100)
        else:
            return 50


    @staticmethod
    def calcular_puntaje_diario(alimentacion, agua, esperanza, sol, aire, sueno, despertar, ejercicio):
        puntajes = [
            AnalizadorHabitosVida.clasificar_alimentacion(alimentacion['tipo_alimento'], alimentacion['saludable']),
            AnalizadorHabitosVida.clasificar_consumo_agua(agua['cantidad']),
            AnalizadorHabitosVida.clasificar_esperanza(esperanza['tipo_practica']),
            AnalizadorHabitosVida.clasificar_sol(sol['tiempo']),
            AnalizadorHabitosVida.clasificar_aire(aire['tiempo']),
            AnalizadorHabitosVida.clasificar_sueno(sueno['hora_dormir'], sueno['hora_despertar']),
            AnalizadorHabitosVida.clasificar_despertar(despertar['estado']),
            AnalizadorHabitosVida.clasificar_ejercicio(ejercicio['tipo'], ejercicio['tiempo'])
        ]
        
        puntaje_total = sum(puntajes) / len(puntajes)  # Promedio de puntajes sobre 100
        return puntaje_total  # Devuelve el puntaje total promedio sobre 100
