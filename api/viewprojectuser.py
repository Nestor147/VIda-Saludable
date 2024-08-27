from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Proyecto, UsuarioProyecto, DatosUsuario
from .serializers import DatosUsuarioSerializer

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
        datos = DatosUsuario.objects.filter(user_id__in=usuarios_ids, tipo='inicial')  # O 'final' según sea necesario
        serializer = DatosUsuarioSerializer(datos, many=True)
        return Response(serializer.data)
