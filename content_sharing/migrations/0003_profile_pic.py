# Generated by Django 5.0.4 on 2024-05-06 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_sharing', '0002_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]