# Generated by Django 3.0.7 on 2020-06-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_auto_20200606_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geo',
            name='lat',
            field=models.CharField(blank=True, max_length=15, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='geo',
            name='long',
            field=models.CharField(blank=True, max_length=15, verbose_name='Долгота'),
        ),
    ]