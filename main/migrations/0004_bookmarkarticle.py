# Generated by Django 3.1.6 on 2021-03-31 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210331_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article', verbose_name='Статья')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'db_table': 'bookmark_article',
            },
        ),
    ]
