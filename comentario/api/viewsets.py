from rest_framework import viewsets

from comentario.api.serializers import ComentarioSerializer
from comentario.models import Comentario


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
