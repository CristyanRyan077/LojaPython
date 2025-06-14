# Generated by Django 5.2.1 on 2025-06-01 21:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0008_produto_descricao_produto_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pagamento', models.CharField(choices=[('credito', 'Cartão de crédito'), ('debito', 'Cartão de débito'), ('pix', 'Pix')], max_length=10)),
                ('endereco', models.CharField(max_length=255)),
                ('data_compra', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto')),
            ],
        ),
    ]
