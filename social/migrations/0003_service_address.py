# Generated by Django 2.2.24 on 2022-04-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20220423_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]