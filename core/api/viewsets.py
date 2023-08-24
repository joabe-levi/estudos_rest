from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from atracao.models import Atracao
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    search_fields = ('nome', 'descricao', 'aprovado')

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk):
        return Response({'teste': 1})

    @action(methods=['post'], detail=True)
    def associar_atracoes(self, request, pk):
        atracoes = request.data.get('ids')
        if not atracoes:
            return Response({'error': 'Informe as atrações!'}, status=400)

        self.get_object().atracoes.set(atracoes)

        return Response({'success': 'Atrações vinculadas com sucesso!'}, status=200)
