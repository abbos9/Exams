# Generated by Django 5.0 on 2023-12-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='main',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
