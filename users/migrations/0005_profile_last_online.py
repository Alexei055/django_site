# Generated by Django 3.1.6 on 2021-02-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210204_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_online',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
