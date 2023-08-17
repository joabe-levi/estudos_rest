from rest_framework import serializers

from avaliacao.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'user', 'comentario', 'nota', 'data')
