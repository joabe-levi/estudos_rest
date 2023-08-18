from rest_framework import serializers

from atracao.models import Atracao


class AtracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'horario_funcionamento', 'idade_minima', 'foto')
