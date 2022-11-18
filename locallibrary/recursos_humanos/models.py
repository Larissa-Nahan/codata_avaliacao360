from email.policy import default
from django.db import models   
from datetime import datetime 
    
class Usuario(models.Model):
    FUNCAO = (
        ('chefe', "Chefe"),
        ('gerente', "Gerente"),
        ('empregado', "Empregado"),
        ('recursos_humanos', "Recursos Humanos"),
    )

    CLASSE = (
        ('a', "A"),
        ('b', "B"),
        ('c', "C"),
        ('d', "D"),
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
        ('xiii', "XIII"),
        ('xiv', "XIV"),
        ('xv', "XV"),
    )

    DIRETORIA = (
        ('diretoria1', "Diretoria 1"),
        ('diretoria2', "Diretoria 2"),
        ('diretoria3', "Diretoria 3"),
        ('diretoria4', "Diretoria 4"),
    )

    GERENCIA = (
        ('gerencia1', "Gerencia 1"),
        ('gerencia2', "Gerencia 2"),
        ('gerencia3', "Gerencia 3"),
        ('gerencia4', "Gerencia 4"),
    )

    GRUPO = (
        ('grupo1', "Grupo 1"),
        ('grupo2', "Grupo 2"),
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
    grupo = models.CharField(max_length=40, choices=GRUPO)
    funcao = models.CharField(max_length=20, choices=FUNCAO)
    classe = models.CharField(max_length=16, choices=CLASSE)
    gerencia = models.CharField(max_length=50, choices=GERENCIA)
    diretoria = models.CharField(max_length=40, choices=DIRETORIA)
    nivel = models.CharField(max_length=5, choices=NIVEL, blank=True, null=True)
    efetivo = models.BooleanField()
    inativo = models.BooleanField()

    class Meta:
        verbose_name = "Usuário"

    def __str__(self) -> str:
        return self.nome

class Avaliacao(models.Model):
    nome = models.ForeignKey(Usuario, related_name='+', on_delete=models.DO_NOTHING)
    cpf = models.ForeignKey(Usuario, related_name='+', on_delete=models.DO_NOTHING)