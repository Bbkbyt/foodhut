# Generated by Django 4.2.3 on 2023-07-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservemodel',
            name='date',
            field=models.DateField(default='2023-01-01', verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='reservemodel',
            name='time',
            field=models.TimeField(default='08:00', verbose_name='ساعت'),
        ),
    ]