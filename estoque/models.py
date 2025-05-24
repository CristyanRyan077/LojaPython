from django.db import models


class produto(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.quantidade} unidades - R${self.preco:.2f}"
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"Cliente: {self.nome} | Telefone: {self.telefone}"
