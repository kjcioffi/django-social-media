# Generated by Django 5.0.3 on 2024-03-13 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_sharing', '0011_replylike'),
    ]

    operations = [
        migrations.AddField(
            model_name='replylike',
            name='reply',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='content_sharing.reply'),
            preserve_default=False,
        ),
    ]
