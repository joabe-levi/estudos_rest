def reprovar_comentarios(modeladmin, reques, queryset):
    queryset.update(aprovado=False)


def aprovar_comentarios(modeladmin, reques, queryset):
    queryset.update(aprovado=True)


reprovar_comentarios.short_description = 'Reprovar Comentários'
aprovar_comentarios.short_description = 'Aprovar Comentários'
