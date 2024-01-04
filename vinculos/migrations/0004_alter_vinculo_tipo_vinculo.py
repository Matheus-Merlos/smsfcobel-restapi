# Generated by Django 5.0.1 on 2024-01-04 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinculos', '0003_tipovinculo_vinculo_tipo_vinculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculo',
            name='tipo_vinculo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='vinculos.tipovinculo'),
            preserve_default=False,
        ),
    ]
