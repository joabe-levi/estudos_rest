from rest_framework import serializers
from core.models import PontoTuristico
from atracao.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = serializers.SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco',
            'descricao_completa'
        )

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'
