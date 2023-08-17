from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Avaliacao(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Usuário'), on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True, verbose_name=_('Comentário'))
    nota = models.DecimalField(max_digits=3, decimal_places=2, verbose_name=_('Nota'))
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        db_table = 'avaliacao'
