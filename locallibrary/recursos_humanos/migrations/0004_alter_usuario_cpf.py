# Generated by Django 4.1.3 on 2022-11-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_humanos', '0003_remove_usuario_matricula_alter_usuario_inativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
