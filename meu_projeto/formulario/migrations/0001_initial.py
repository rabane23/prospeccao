# Generated by Django 4.2.3 on 2023-07-16 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RespostaFormulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipamento', models.CharField(max_length=100)),
                ('qual_linha', models.CharField(max_length=100)),
                ('extensao', models.CharField(max_length=100)),
                ('extensao_sem_leitura', models.CharField(max_length=100)),
                ('espacamento_medio', models.CharField(max_length=100)),
                ('tipo_dormente', models.CharField(max_length=100)),
                ('quantidade_dormentes_intercalados', models.CharField(max_length=100)),
                ('tipo_fixacao', models.CharField(max_length=100)),
                ('proporcao_fixacao_mista', models.CharField(max_length=100)),
                ('tdc', models.CharField(max_length=100)),
                ('concreto', models.CharField(max_length=100)),
                ('isolado_nao_isol', models.CharField(max_length=100)),
                ('malha1', models.CharField(max_length=100)),
                ('malha2', models.CharField(max_length=100)),
                ('malha3', models.CharField(max_length=100)),
                ('malha4', models.CharField(max_length=100)),
                ('malha5', models.CharField(max_length=100)),
                ('malha6', models.CharField(max_length=100)),
                ('malha7', models.CharField(max_length=100)),
                ('malha8', models.CharField(max_length=100)),
                ('malha9', models.CharField(max_length=100)),
                ('malha10', models.CharField(max_length=100)),
            ],
        ),
    ]