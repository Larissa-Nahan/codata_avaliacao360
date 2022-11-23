from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "funcao", "diretoria"]
    filter_horizontal = ('meritos', 'demeritos')
admin.site.register(Usuario, UsuarioAdmin)