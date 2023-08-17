from rest_framework import viewsets

from avaliacao.api.serializers import AvaliacaoSerializer
from avaliacao.models import Avaliacao


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer