from django.contrib import admin
from .models import Usuario, Gerencia, Diretoria

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "funcao", "diretoria"]
    filter_horizontal = ('meritos', 'demeritos')
admin.site.register(Usuario, UsuarioAdmin)

class GerenciaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gerencia, GerenciaAdmin)

class DiretoriaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Diretoria, DiretoriaAdmin)