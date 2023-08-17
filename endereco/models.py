from django.db import models
from django.utils.translation import gettext_lazy as _


class Endereco(models.Model):
    rua = models.CharField(max_length=200, verbose_name=_('Rua'))
    complemento = models.CharField(max_length=200, verbose_name=_('Complemento'), null=True, blank=True)
    cidade = models.CharField(max_length=200, verbose_name=_('Cidade'))
    estado = models.CharField(max_length=150, verbose_name=_('Estado'))
    pais = models.CharField(max_length=150, verbose_name=_('País'))
    latitude = models.IntegerField(verbose_name=_('Latitude'), null=True, blank=True)
    longitude = models.IntegerField(verbose_name=_('Longitude'), null=True, blank=True)

    def __str__(self):
        if self.complemento:
            return f'{self.rua} - {self.complemento}'
        return self.rua

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        db_table = 'endereco'
