# Generated by Django 4.0.4 on 2022-04-27 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_plant_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soil',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]