# Generated by Django 2.2.24 on 2022-05-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_auto_20220507_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default='istanbul', max_length=255),
        ),
    ]
