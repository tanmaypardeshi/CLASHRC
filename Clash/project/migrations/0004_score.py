# Generated by Django 2.0.1 on 2019-08-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
