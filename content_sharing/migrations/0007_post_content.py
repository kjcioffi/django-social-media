# Generated by Django 5.0.4 on 2024-05-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_sharing', '0006_rename_user_post_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(default=''),
            preserve_default=False,
        ),
    ]
