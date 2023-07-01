# Generated by Django 4.1.3 on 2023-02-27 22:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_diaria_motivo_cancelamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaria',
            name='candidatos',
        ),
        migrations.AddField(
            model_name='diaria',
            name='candidatas',
            field=models.ManyToManyField(blank=True, related_name='candidatas', to=settings.AUTH_USER_MODEL),
        ),
    ]
