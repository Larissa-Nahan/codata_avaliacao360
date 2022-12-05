from django import forms
from .models import Usuario, Gerencia, Diretoria
from avaliacao.models import FatorDesempenhoMerito, FatorDesempenhoDemerito

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class CadastrarUsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gerencia'].queryset = Gerencia.objects.none()

        data_admissao_usuario = forms.DateField(input_formats='%d/%m/%Y')

        if 'diretoria' in self.data:
            try:
                id_diretoria = int(self.data.get('diretoria'))
                self.fields['gerencia'].queryset = Gerencia.objects.filter(diretoria_id=id_diretoria).order_by('gerencia')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Gerencia queryset
        elif self.instance.pk:
            self.fields['gerencia'].queryset = self.instance.diretoria.gerencia_set.order_by('gerencia')

    class Meta:
        model = Usuario
        fields = ['efetivo', 'diretoria', 'gerencia', 'funcao', 'data_admissao_usuario', 'nome', 'cpf', 'matricula', 'nivel']

class EditarUsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gerencia'].queryset = Gerencia.objects.none()

        data_admissao_usuario = forms.DateField(input_formats='%d/%m/%Y')

        if 'diretoria' in self.data:
            try:
                id_diretoria = int(self.data.get('diretoria'))
                self.fields['gerencia'].queryset = Gerencia.objects.filter(diretoria_id=id_diretoria).order_by('gerencia')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Gerencia queryset
        elif self.instance.pk:
            self.fields['gerencia'].queryset = self.instance.diretoria.gerencia_set.order_by('gerencia')
            
    class Meta:
        model = Usuario
        fields = ['efetivo', 'inativo', 'diretoria', 'gerencia', 'funcao', 'data_admissao_usuario', 'nome', 'cpf', 'matricula', 'nivel']


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