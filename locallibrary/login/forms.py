from django.forms import ModelForm, TextInput, PasswordInput
from .models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['cpf', 'senha']
        widgets = {
            'cpf' : TextInput(attrs={'placeholder': 'CPF Usuario'}),
            'senha' : PasswordInput(attrs={'placeholder': 'Senha', 'data-toggle': 'password'}),
        }

class RecuperarSenhaForm(ModelForm):
    class Meta:
        model = Login
        fields = ['email']

class NovaSenhaForm(ModelForm):
    class Meta:
        model = Login
        fields = ['senha']