# Generated by Django 3.2.7 on 2021-12-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expcard', '0003_alter_position_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='periods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_period', models.CharField(max_length=30, verbose_name='Название периода')),
                ('date_start', models.DateTimeField(verbose_name='Дата начала периода')),
                ('date_end', models.DateTimeField(verbose_name='Дата окончания периода')),
            ],
            options={
                'verbose_name': 'Период',
                'verbose_name_plural': 'Периоды',
            },
        ),
    ]