# Generated by Django 4.2.3 on 2023-07-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0005_alter_respostaformulario_extensao_sem_leitura_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='respostaformulario',
            name='Furo_NOK',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Isolador_Falta',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Isolador_NOK',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Palmilha_Falta',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Palmilha_NOK',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Placa_Falta',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Placa_NOK',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Shoulder_Falta',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Shoulder_NOK',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Tirefond_Falta',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='Tirefond_NOK',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
