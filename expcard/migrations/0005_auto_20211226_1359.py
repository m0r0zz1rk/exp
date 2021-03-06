# Generated by Django 3.2.7 on 2021-12-26 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expcard', '0004_periods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certified',
            name='month',
        ),
        migrations.RemoveField(
            model_name='certified',
            name='year',
        ),
        migrations.AddField(
            model_name='certified',
            name='period',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='expcard.periods', verbose_name='Период'),
        ),
        migrations.AddField(
            model_name='criteria_export',
            name='period',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='expcard.periods', verbose_name='Период'),
        ),
        migrations.AddField(
            model_name='expcards',
            name='period',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='expcard.periods', verbose_name='Период'),
        ),
        migrations.AddField(
            model_name='summary_table',
            name='period',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='expcard.periods', verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='delegates',
            name='period',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='expcard.periods', verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='specialists',
            name='period',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='expcard.periods', verbose_name='Период'),
        ),
    ]
