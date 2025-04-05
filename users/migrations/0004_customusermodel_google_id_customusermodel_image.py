# Generated by Django 5.1.4 on 2025-04-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customusermodel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='google_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
