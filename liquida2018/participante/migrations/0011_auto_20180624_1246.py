# Generated by Django 2.0.6 on 2018-06-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0010_auto_20180624_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentofiscal',
            name='compradoMASTERCARD',
            field=models.BooleanField(default=False, verbose_name='Comprou com MASTERCARD?'),
        ),
        migrations.AlterField(
            model_name='documentofiscal',
            name='compradoREDE',
            field=models.BooleanField(default=False, verbose_name='Comprou na maquininha da REDE?'),
        ),
        migrations.AlterField(
            model_name='documentofiscal',
            name='observacao',
            field=models.TextField(blank=True, default='Nenhuma', max_length=1000, null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='documentofiscal',
            name='pendente',
            field=models.BooleanField(default=True, verbose_name='Pendente'),
        ),
    ]
