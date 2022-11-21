from django.contrib import admin
from .models import Usuario, Classe, Nivel, Gerencia, Diretoria, Grupo

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "funcao", "diretoria"]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "meritos":
            kwargs["queryset"] = Usuario.objects.filter(nome=request.user)
        return super(UsuarioAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

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
