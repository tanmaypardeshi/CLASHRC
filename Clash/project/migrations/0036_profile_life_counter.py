# Generated by Django 2.2.3 on 2019-09-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0035_auto_20190909_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='life_counter',
            field=models.IntegerField(default=0),
        ),
    ]
