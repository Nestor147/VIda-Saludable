from rest_framework import serializers
from .models import (
    Role, Usuario, Alimentacion, Agua, Esperanza, Sol, Aire, Dormir,
    Despertar, Ejercicio, Proyecto, UsuarioProyecto, DatosUsuario
)

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class UsuarioProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioProyecto
        fields = '__all__'


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
        fields ='__all__'


class DormirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormir
        fields = '__all__'


class DespertarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despertar
        fields ='__all__'


class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'




class DatosUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosUsuario
        fields = '__all__'



class UsuarioWithRoleSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ['id', 'name', 'last_name', 'phone', 'email', 'password','role_name']  # Incluye los campos que necesitas

    def get_role_name(self, obj):
        return obj.role.name if obj.role else None