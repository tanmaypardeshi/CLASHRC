# Generated by Django 2.2.3 on 2019-09-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_auto_20190906_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bon_que_timer',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bon_score',
            field=models.IntegerField(default=32),
        ),
    ]
