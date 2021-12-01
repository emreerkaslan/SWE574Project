# Generated by Django 2.2.24 on 2021-12-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_auto_20211201_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventpicture',
            field=models.ImageField(default='uploads/event_pictures/default.png', upload_to='uploads/event_pictures/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='picture',
            field=models.ImageField(default='uploads/service_pictures/default.png', upload_to='uploads/service_pictures/'),
        ),
    ]
