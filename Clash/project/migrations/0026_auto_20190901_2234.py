# Generated by Django 2.2.3 on 2019-09-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0025_auto_20190901_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='visited',
            field=models.CharField(default='', max_length=100),
        ),
    ]
