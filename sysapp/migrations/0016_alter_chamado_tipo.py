# Generated by Django 4.2.7 on 2023-12-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysapp', '0015_alter_chamado_categoria_alter_chamado_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='tipo',
            field=models.CharField(choices=[('Suporte', 'Suporte'), ('Financeiro', 'Financeiro'), ('Outros', 'Outros')], max_length=20, null=True),
        ),
    ]
