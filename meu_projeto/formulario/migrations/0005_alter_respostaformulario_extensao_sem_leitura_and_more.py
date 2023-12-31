# Generated by Django 4.2.3 on 2023-07-17 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0004_alter_respostaformulario_extensao_sem_leitura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respostaformulario',
            name='extensao_sem_leitura',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='guarda',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='junta',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha10',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha7',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha8',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='malha9',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='proporcao_fixacao_mista',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='quantidade_dormentes_intercalados',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='respostaformulario',
            name='solda',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
