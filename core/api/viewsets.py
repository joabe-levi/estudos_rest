from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    # filterset_fields = ('nome', 'descricao', 'aprovado')
    search_fields = ('nome', 'descricao', 'aprovado')

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk):
        return Response({'teste': 1})
