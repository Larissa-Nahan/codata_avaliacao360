from django import forms
from recursos_humanos.models import Usuario

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cpf', 'senha']

class RecuperarSenhaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email']

class NovaSenhaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['senha']