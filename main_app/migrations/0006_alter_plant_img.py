# Generated by Django 4.0.4 on 2022-04-27 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_soil_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]
