from django.db import models

class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    codigo_referencia = models.CharField(max_length=50, unique=True)
    localizacao = models.CharField(max_length=100, blank=True)  # Ex: "Prateleira A3"
    quantidade = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=1)
    fabricante = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo_referencia})"

    def em_falta(self):
        return self.quantidade < self.estoque_minimo
