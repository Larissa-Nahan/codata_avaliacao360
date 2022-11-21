from email.policy import default
from django.db import models   
from datetime import datetime 
from avaliacao.models import FatorDesempenhoMerito, FatorDesempenhoDemerito

class Classe(models.Model):
    classe = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.classe

class Nivel(models.Model):
    nivel = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.nivel

class Gerencia(models.Model):
    gerencia = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.gerencia

class Diretoria(models.Model):
    diretoria = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.diretoria

class Grupo(models.Model):
    grupo = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.grupo

class Usuario(models.Model):
    FUNCAO = (
        ('chefe', "Chefe"),
        ('gerente', "Gerente"),
        ('empregado', "Empregado"),
        ('recursos_humanos', "Recursos Humanos"),
    )

    nome = models.CharField(max_length=100, blank=False, null=False)
    senha = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    
    data_criacao_usuario = models.DateField(default=datetime.now, blank=False, null=False)
    data_atualizacao_usuario = models.DateField(blank=True, null=True)
    data_exclusao_usuario = models.DateField(blank=True, null=True)   
    ultima_avaliacao = models.DateField(blank=True, null=True)
    
    setor = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    funcao = models.CharField(max_length=20, choices=FUNCAO)
    classe = models.ForeignKey(Classe, blank=True, null=True, on_delete=models.SET_NULL)
    nivel = models.ForeignKey(Nivel, blank=True, null=True, on_delete=models.SET_NULL)
    gerencia = models.ForeignKey(Gerencia, blank=True, null=True, on_delete=models.SET_NULL)
    diretoria = models.ForeignKey(Diretoria, blank=True, null=True, on_delete=models.SET_NULL)
    grupo = models.ForeignKey(Grupo, blank=True, null=True, on_delete=models.SET_NULL)

    efetivo = models.BooleanField(default=False)
    inativo = models.BooleanField(default=False)

    meritos = models.ManyToManyField(FatorDesempenhoMerito, blank=True)
    demeritos = models.ManyToManyField(FatorDesempenhoDemerito, blank=True)


    class Meta:
        verbose_name = "Usuário"

    def __str__(self) -> str:
        return self.nome

class Avaliacao(models.Model):
    nome = models.ForeignKey(Usuario, related_name='+', on_delete=models.DO_NOTHING)
    cpf = models.ForeignKey(Usuario, related_name='+', on_delete=models.DO_NOTHING)
