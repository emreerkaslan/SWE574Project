# Generated by Django 2.2.24 on 2021-12-15 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0026_remove_userprofile_userrating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]