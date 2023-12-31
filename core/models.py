from django.db import models
from django.utils.translation import gettext_lazy as _
from atracao.models import Atracao
from avaliacao.models import Avaliacao
from comentario.models import Comentario
from endereco.models import Endereco


class DocumentoIdentificacao(models.Model):
    descricao = models.CharField(max_length=200, verbose_name=_('Descrição'))
    numero = models.IntegerField(verbose_name=_('Número'))


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=200, verbose_name=_('Nome'))
    descricao = models.TextField(verbose_name=_('Descrição'))
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao, verbose_name=_('Atrações'))
    comentarios = models.ManyToManyField(Comentario, verbose_name=_('Comentários'))
    avaliacoes = models.ManyToManyField(Avaliacao, verbose_name=_('Avaliações'))
    endereco = models.ForeignKey(Endereco, verbose_name=_('Endereço'), on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField(
        DocumentoIdentificacao, null=True, blank=True, on_delete=models.CASCADE,
        verbose_name=_('Documento de Identificação')
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Ponto Turistico'
        verbose_name_plural = 'Pontos Turisticos'
        db_table = 'ponto_turistico'
