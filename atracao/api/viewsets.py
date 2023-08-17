from rest_framework import viewsets
from atracao.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
