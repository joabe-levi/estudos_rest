from rest_framework import viewsets

from endereco.api.serializers import EnderecoSerializer
from endereco.models import Endereco


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer