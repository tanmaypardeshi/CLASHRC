# Generated by Django 2.2.3 on 2019-09-09 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_auto_20190909_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mob2',
            field=models.CharField(default='9999999999', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='p2_email',
            field=models.CharField(default='a@a.com', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='p2_name',
            field=models.CharField(default='a', max_length=100, null=True),
        ),
    ]
