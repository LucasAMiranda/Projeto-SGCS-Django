# Generated by Django 4.2.7 on 2023-12-01 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default='', max_length=128, verbose_name='Senha'),
        ),
    ]
