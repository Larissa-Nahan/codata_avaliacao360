from django import forms
from .models import Usuario
from avaliacao.models import FatorDesempenhoMerito, FatorDesempenhoDemerito

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


class AvaliacaoForm(forms.ModelForm):
    meritos = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = FatorDesempenhoMerito.objects.all(),
    )
    demeritos = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = FatorDesempenhoDemerito.objects.all(),
    )
    
    class Meta:
        model = Usuario
        fields = ['meritos', 'demeritos']