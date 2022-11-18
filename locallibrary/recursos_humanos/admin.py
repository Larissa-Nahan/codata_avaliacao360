from django.contrib import admin
from .models import Usuario, Classe, Nivel, Gerencia, Diretoria, Grupo
from .forms import UsuarioForm

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "funcao", "diretoria"]
    form = UsuarioForm
admin.site.register(Usuario, UsuarioAdmin)

class ClasseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Classe, ClasseAdmin)

class NivelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Nivel, NivelAdmin)

class GerenciaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gerencia, GerenciaAdmin)

class DiretoriaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Diretoria, DiretoriaAdmin)

class GrupoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Grupo, GrupoAdmin)
