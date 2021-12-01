# Generated by Django 2.2.24 on 2021-12-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_auto_20211201_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventpicture',
            field=models.ImageField(blank=True, default='uploads/event_pictures/default.png', upload_to='uploads/event_pictures/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/service_pictures/default.png', upload_to='uploads/service_pictures/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures/'),
        ),
    ]
