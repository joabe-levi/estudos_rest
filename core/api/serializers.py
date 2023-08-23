from rest_framework import serializers

from atracao.models import Atracao
from core.models import PontoTuristico, DocumentoIdentificacao
from atracao.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer
from endereco.models import Endereco


class DocumentoIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = serializers.SerializerMethodField()
    doc_identificacao = DocumentoIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco',
            'descricao_completa', 'doc_identificacao',
        )
        read_only_fields = ('comentarios', 'avaliacoes',)

    def get_or_create_atracao(self, atracao_dict):
        atracao, created = Atracao.objects.get_or_create(**atracao_dict)
        return atracao

    def get_or_create_endereco(self, endereco_dict):
        endereco, created = Endereco.objects.get_or_create(**endereco_dict)
        return endereco

    def get_or_create_documento_identificacao(self, doc_identificaocao_dict):
        return DocumentoIdentificacao.objects.create(**doc_identificaocao_dict)

    def create(self, validated_data):
        atracoes = validated_data.get('atracoes')
        endereco_dict = validated_data.get('endereco')
        doc_identificacao_dict = validated_data.get('doc_identificacao')

        validated_data.pop('atracoes')
        validated_data.pop('endereco')
        validated_data.pop('doc_identificacao')

        ponto_turistico = super().create(validated_data)
        for atracao in atracoes:
            ponto_turistico.atracoes.add(
                self.get_or_create_atracao(atracao)
            )

        ponto_turistico.endereco = self.get_or_create_endereco(endereco_dict)
        ponto_turistico.save()
        if not ponto_turistico.doc_identificacao:
            ponto_turistico.doc_identificacao = self.get_or_create_documento_identificacao(doc_identificacao_dict)
            ponto_turistico.save()
        return ponto_turistico

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'
