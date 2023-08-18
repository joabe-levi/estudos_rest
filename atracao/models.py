from django.db import models
from django.utils.translation import gettext_lazy as _


class Atracao(models.Model):
    nome = models.CharField(max_length=200, verbose_name=_('Nome'))
    descricao = models.TextField(verbose_name=_('Descrição'))
    horario_funcionamento = models.TextField(verbose_name=_('Horário de funcionamento'))
    idade_minima = models.IntegerField(_('Idade mínima'))
    foto = models.ImageField(upload_to='atracoes', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
        db_table = 'atracao'
