from django.forms import ModelForm, TextInput, PasswordInput
from recursos_humanos.models import Usuario

class LoginForm(ModelForm):
    class Meta:
        model = Usuario
        # senha = CharField(label='Search')
        fields = ['cpf', 'senha']
        widgets = {
            'cpf' : TextInput(attrs={'placeholder': 'CPF Usuario'}),
            'senha' : PasswordInput(attrs={'placeholder': 'Senha', 'data-toggle': 'password'}),
        }

class RecuperarSenhaForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email']

class NovaSenhaForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['senha']