# Generated by Django 5.0 on 2023-12-11 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_info', '0002_weather_name_alter_weather_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='country',
            new_name='humidity',
        ),
    ]
