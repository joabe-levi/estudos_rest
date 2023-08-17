from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Comentario(models.Model):
    usuario = models.ForeignKey(User, verbose_name=_('Usuário'), on_delete=models.CASCADE)
    comentario = models.TextField(_('Comentário'))
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    aprovado = models.BooleanField(default=True, verbose_name=_('Aprovado'))

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        db_table = 'comentario'
