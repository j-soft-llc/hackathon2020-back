# Generated by Django 3.0.7 on 2020-06-06 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200606_1927'),
        ('initiative', '0002_geo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Geo',
        ),
    ]
