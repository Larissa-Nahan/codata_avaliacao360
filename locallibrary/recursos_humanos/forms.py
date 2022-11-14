from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class CadastrarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['efetivo', 'diretoria', 'gerencia', 'funcao', 'nome', 'cpf', 'nivel']

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['efetivo', 'inativo', 'diretoria', 'gerencia', 'funcao', 'nome', 'cpf', 'nivel']