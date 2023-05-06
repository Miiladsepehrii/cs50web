# Generated by Django 3.2 on 2021-09-20 20:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_user_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='users_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='user_followers', to=settings.AUTH_USER_MODEL),
        ),
    ]