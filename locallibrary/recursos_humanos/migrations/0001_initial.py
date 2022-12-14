# Generated by Django 4.1.3 on 2022-11-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=11)),
                ('data_criacao_usuario', models.DateField()),
                ('data_atualizacao_usuario', models.DateField(blank=True, null=True)),
                ('data_exclusao_usuario', models.DateField(blank=True, null=True)),
                ('setor', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('grupo', models.CharField(choices=[('grupo1', 'Grupo 1'), ('grupo2', 'Grupo 2')], max_length=40)),
                ('funcao', models.CharField(choices=[('chefe', 'Chefe'), ('gerente', 'Gerente'), ('empregado', 'Empregado'), ('recursos_humanos', 'Recursos Humanos')], max_length=20)),
                ('classe', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=16)),
                ('diretoria', models.CharField(choices=[('diretoria1', 'Diretoria 1'), ('diretoria2', 'Diretoria 2'), ('diretoria3', 'Diretoria 3'), ('diretoria4', 'Diretoria 4')], max_length=40)),
                ('gerencia', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=8)),
                ('nivel', models.CharField(blank=True, choices=[('i', 'I'), ('ii', 'II'), ('iii', 'III'), ('iv', 'IV'), ('v', 'V'), ('vi', 'VI'), ('vii', 'VII'), ('viii', 'VIII'), ('ix', 'IX'), ('x', 'X'), ('xi', 'XI'), ('xii', 'XII'), ('xiii', 'XIII'), ('xiv', 'XIV'), ('xv', 'XV')], max_length=5, null=True)),
                ('efetivo', models.BooleanField()),
                ('inativo', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Usu??rio',
            },
        ),
    ]
