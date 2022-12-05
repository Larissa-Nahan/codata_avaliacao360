from email.policy import default
from django.db import models   
from datetime import datetime 
from avaliacao.models import FatorDesempenhoMerito, FatorDesempenhoDemerito, AvaliacaoDesempenho


class Diretoria(models.Model):
    diretoria = models.CharField(max_length=100, blank=False, null=False)
    sigla = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self) -> str:
        return self.diretoria

class Gerencia(models.Model):
    gerencia = models.CharField(max_length=100, blank=False, null=False)
    diretoria = models.ForeignKey(Diretoria, on_delete=models.CASCADE)
   
    class Meta:
        verbose_name = "Gerência"

    def __str__(self) -> str:
        return self.gerencia

class Usuario(models.Model):
    FUNCAO = (
        ('presidente', "Presidente"),
        ('diretos', "Diretor"),
        ('gerente', "Gerente"),
        ('chefe', "Chefe"),
        ('colaborador', "Colaborador"),
        ('cedido', "Cedido a outro orgão"),
        ('recursos_humanos', "Recursos Humanos"),
    )

    CLASSE = (
        ('classe1', "Classe 1"),
        ('classe2', "Classe 2"),
        ('classe3', "Classe 3"),
    )

    NIVEL = (
        ('', '----'),
        ('i', "I"),
        ('ii', "II"),
        ('iii', "III"),
        ('iv', "IV"),
        ('v', "V"),
        ('vi', "VI"),
        ('vii', "VII"),
        ('viii', "VIII"),
        ('ix', "IX"),
        ('x', "X"),
        ('xi', "XI"),
        ('xii', "XII"),
    )

    nome = models.CharField(max_length=100, blank=False, null=False)
    senha = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=True, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    matricula = models.CharField(max_length=8, blank=True, null=True)
    
    data_criacao_usuario = models.DateField(default=datetime.now, blank=False, null=False)
    data_admissao_usuario = models.DateField(blank=True, null=True)
    data_atualizacao_usuario = models.DateField(blank=True, null=True)
    data_inativacao_usuario = models.DateField(blank=True, null=True)   
    data_ultima_avaliacao = models.DateField(blank=True, null=True)
    
    setor = models.CharField(max_length=50, blank=True)
    cargo = models.CharField(max_length=50, blank=True)
    funcao = models.CharField(max_length=20, choices=FUNCAO)
    classe = models.CharField(max_length=20, choices=CLASSE)
    nivel = models.CharField(max_length=5, choices=NIVEL, blank=True, null=True)
    
    gerencia = models.ForeignKey('Gerencia', on_delete=models.CASCADE)
    diretoria = models.ForeignKey('Diretoria', on_delete=models.CASCADE)

    efetivo = models.BooleanField(default=False)
    inativo = models.BooleanField(default=False)

    meritos = models.ManyToManyField(FatorDesempenhoMerito, blank=True)
    demeritos = models.ManyToManyField(FatorDesempenhoDemerito, blank=True)

    avaliacoes = models.ManyToManyField(AvaliacaoDesempenho, blank=True)


    class Meta:
        verbose_name = "Usuário"

    def __str__(self) -> str:
        return self.nome
