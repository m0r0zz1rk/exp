# Generated by Django 3.2.7 on 2021-12-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expcard', '0005_auto_20211226_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periods',
            name='date_end',
            field=models.DateField(verbose_name='Дата окончания периода'),
        ),
        migrations.AlterField(
            model_name='periods',
            name='date_start',
            field=models.DateField(verbose_name='Дата начала периода'),
        ),
    ]
