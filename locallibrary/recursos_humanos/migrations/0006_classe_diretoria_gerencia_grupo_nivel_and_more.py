# Generated by Django 4.1.3 on 2022-11-18 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_humanos', '0005_usuario_ultima_avaliacao_avaliacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Diretoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diretoria', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerencia', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='inativo',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='classe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recursos_humanos.classe'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='diretoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recursos_humanos.diretoria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='gerencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recursos_humanos.gerencia'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recursos_humanos.grupo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nivel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recursos_humanos.nivel'),
        ),
    ]
