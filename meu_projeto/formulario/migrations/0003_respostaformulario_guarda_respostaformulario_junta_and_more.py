# Generated by Django 4.2.3 on 2023-07-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_alter_respostaformulario_tdc'),
    ]

    operations = [
        migrations.AddField(
            model_name='respostaformulario',
            name='guarda',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='junta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respostaformulario',
            name='solda',
            field=models.IntegerField(default=0),
        ),
    ]
