from django.contrib import admin
from .models import Usuario
from .forms import UsuarioForm

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "funcao", "diretoria"]
    form = UsuarioForm

admin.site.register(Usuario, UsuarioAdmin)
