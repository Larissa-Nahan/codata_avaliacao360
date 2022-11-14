# Generated by Django 4.1.3 on 2022-11-11 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_humanos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='data_criacao_usuario',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='gerencia',
            field=models.CharField(choices=[('gerencia1', 'Gerencia 1'), ('gerencia2', 'Gerencia 2'), ('gerencia3', 'Gerencia 3'), ('gerencia4', 'Gerencia 4')], max_length=50),
        ),
    ]
