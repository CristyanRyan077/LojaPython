from django.db import models


class produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.quantidade} unidades - R${self.preco:.2f}"

class Compra(models.Model):
    METODOS_PAGAMENTO = [
        ('credito', 'Cartão de crédito'),
        ('debito', 'Cartão de débito'),
        ('pix', 'Pix'),
    ]
    produto = models.ForeignKey(produto, on_delete=models.CASCADE)
    metodo_pagamento = models.CharField(max_length=10, choices=METODOS_PAGAMENTO)
    endereco = models.CharField(max_length=255)
    data_compra = models.DateTimeField(auto_now_add=True)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"Cliente: {self.nome} | Telefone: {self.telefone}"
    
