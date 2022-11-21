from django.db import models  

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome_categoria

class AvaliacaoDesempenho(models.Model):
    avaliacao_otima = models.TextField()
    avaliacao_boa = models.TextField()
    avaliacao_regular = models.TextField()
    avaliacao_insuficiente = models.TextField()
    categoria_avaliacao = models.OneToOneField(Categoria, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Avaliação de Desempenho"
        verbose_name_plural = "Avaliações de Desempenho"

    def __str__(self) -> str:
        return f"Critério {self.categoria_avaliacao}"


class FatorDesempenhoMerito(models.Model):
    fator = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Fator de Desempenho Meritório"

    def __str__(self) -> str:
        return self.fator

class FatorDesempenhoDemerito(models.Model):
    fator = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Fator de Desempenho Demeritório"
        verbose_name_plural = "Fator de Desempenho Demeritórios"

    def __str__(self) -> str:
        return self.fator