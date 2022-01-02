# Generated by Django 2.2.24 on 2021-12-25 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0030_auto_20211225_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotifyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField(blank=True, null=True)),
                ('hasRead', models.BooleanField(default=False)),
                ('notify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]