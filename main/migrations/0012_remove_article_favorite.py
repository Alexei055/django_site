# Generated by Django 3.2.2 on 2021-05-19 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='favorite',
        ),
    ]
