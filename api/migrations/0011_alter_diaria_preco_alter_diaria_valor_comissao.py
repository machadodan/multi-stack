# Generated by Django 4.1.3 on 2023-02-27 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_diaria_candidatos_diaria_candidatas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaria',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='diaria',
            name='valor_comissao',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
