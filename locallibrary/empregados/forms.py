from django.forms import ModelForm, TextInput, PasswordInput
from recursos_humanos.models import Usuario

class Avaliacao(ModelForm):
    class Meta:
        model = Usuario
        fields = ['efetivo', 'diretoria', 'gerencia', 'funcao', 'nome', 'cpf', 'nivel']
        widgets = {
            'cpf' : TextInput(attrs={'placeholder': 'CPF Usuario'}),
            'senha' : PasswordInput(attrs={'placeholder': 'Senha', 'data-toggle': 'password'}),
        }