from rest_framework import serializers
from .models import Usuario, Alimentacion, Agua, Esperanza, Sol, Aire, Sleep, Despertar, Ejercicio

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'name', 'last_name', 'phone', 'email', 'password_hash', 'created_at', 'updated_at']

class AlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacion
        fields = '__all__'

class AguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agua
        fields = '__all__'

class EsperanzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esperanza
        fields = '__all__'

class SolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sol
        fields = '__all__'

class AireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aire
        fields = '__all__'

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = '__all__'

class DespertarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despertar
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'
