# Generated by Django 5.0.4 on 2024-04-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='priority',
            field=models.IntegerField(choices=[('Very Urgent', 1), ('Urgent', 2), ('Normal', 3), ('Not Urgent', 4), ('Very Not Urgent', 5)], default='Normal'),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='priority',
            field=models.IntegerField(choices=[('Very Urgent', 1), ('Urgent', 2), ('Normal', 3), ('Not Urgent', 4), ('Very Not Urgent', 5)], default='Normal'),
        ),
    ]