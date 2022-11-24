from email.policy import default
from django.db import models   
from datetime import datetime 
from avaliacao.models import FatorDesempenhoMerito, FatorDesempenhoDemerito, AvaliacaoDesempenho

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

    GERENCIA = (
        ('adminstrativa', "Adminstrativa"),
        ('financeira', "Financeira"),
        ('negocios_prospeccao', "Negócios e Prospecção"),
        ('treinamento', "Treinamento"),
        ('recursos_humanos', "Recursos Humanos"),
    )

    DIRETORIA = (
        ('diraf', "Diretoria Administrativa Financeira"),
        ('dides', "Diretoria de Desenvolvimento de Sistemas"),
        ('dirad', "Diretoria de Alto Desempenho"),
        ('ditec', "Diretoria de Tecnologia da Informação e Comunicação"),
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
    classe = models.CharField(max_length=20, choices=CLASSE)
    nivel = models.CharField(max_length=5, choices=NIVEL)
    gerencia = models.CharField(max_length=20, choices=GERENCIA)
    diretoria = models.CharField(max_length=20, choices=DIRETORIA)

    efetivo = models.BooleanField(default=False)
    inativo = models.BooleanField(default=False)

    meritos = models.ManyToManyField(FatorDesempenhoMerito, blank=True)
    demeritos = models.ManyToManyField(FatorDesempenhoDemerito, blank=True)

    avaliacoes = models.ManyToManyField(AvaliacaoDesempenho, blank=True)


    class Meta:
        verbose_name = "Usuário"

    def __str__(self) -> str:
        return self.nome
