# Generated by Django 5.0.4 on 2024-04-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0004_alter_bugreport_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='priority',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='priority',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3),
        ),
    ]