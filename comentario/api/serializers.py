from rest_framework import serializers

from comentario.models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'data', 'aprovado')
