# Generated by Django 5.2.1 on 2025-05-25 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_alter_produto_nome_alter_produto_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(),
        ),
    ]
