# Generated by Django 4.2.7 on 2023-12-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysapp', '0014_chamado_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Informática', 'Informática'), ('Redes', 'Redes'), ('Segurança', 'Segurança'), ('Outros', 'Outros')], max_length=20),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='titulo',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
