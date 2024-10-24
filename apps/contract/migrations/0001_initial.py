# Generated by Django 5.0.6 on 2024-10-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.IntegerField(blank=True, null=True, verbose_name='ARCGIS OBJ ID')),
                ('num', models.CharField(blank=True, max_length=256, null=True, verbose_name='Номер договора')),
                ('exp_date', models.DateField(blank=True, null=True, verbose_name='Дата истечения договора')),
                ('location', models.CharField(blank=True, max_length=256, null=True, verbose_name='Локация')),
                ('area', models.FloatField(blank=True, null=True, verbose_name='Площадь')),
                ('price_1sq', models.IntegerField(blank=True, null=True, verbose_name='Стоимость 1 кв м')),
                ('montly', models.IntegerField(blank=True, null=True, verbose_name='Оплата за месяц')),
                ('tenant', models.CharField(blank=True, max_length=512, null=True, verbose_name='Владелец')),
                ('purpose', models.CharField(blank=True, max_length=512, null=True, verbose_name='Назначение')),
                ('num_date_agg', models.CharField(blank=True, max_length=512, null=True, verbose_name='Номер и дата договора')),
                ('subrent', models.CharField(blank=True, max_length=512, null=True, verbose_name='Субаренда')),
                ('owner_ddu', models.CharField(blank=True, max_length=512, null=True, verbose_name='')),
                ('note', models.CharField(blank=True, max_length=512, null=True, verbose_name='Примечание')),
                ('region', models.CharField(blank=True, max_length=512, null=True, verbose_name='Регион')),
                ('globalid', models.CharField(blank=True, max_length=128, null=True, verbose_name='GLOBAL ID')),
                ('phone_num', models.CharField(blank=True, max_length=64, null=True, verbose_name='Номер телефона владельца')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'Договора',
            },
        ),
    ]
