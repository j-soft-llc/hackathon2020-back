# Generated by Django 3.0.7 on 2020-06-06 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initiative', '0002_geo'),
        ('users', '0003_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_geo', to='initiative.Geo'),
        ),
        migrations.AddField(
            model_name='user',
            name='сompetencies',
            field=models.ManyToManyField(related_name='categories', to='initiative.Category'),
        ),
    ]
