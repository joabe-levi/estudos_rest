from django.contrib import admin
from .models import Comentario
from .actions import reprovar_comentarios, aprovar_comentarios


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data', 'aprovado')
    actions = (reprovar_comentarios, aprovar_comentarios)


admin.site.register(Comentario, ComentarioAdmin)
