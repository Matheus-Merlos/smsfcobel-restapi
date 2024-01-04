# Generated by Django 5.0.1 on 2024-01-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinculos', '0004_alter_vinculo_tipo_vinculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cns',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='rg',
            field=models.IntegerField(unique=True),
        ),
    ]
