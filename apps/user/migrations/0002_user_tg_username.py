# Generated by Django 5.0.6 on 2024-10-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_username',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Логин в тг'),
        ),
    ]