# Generated by Django 3.1.6 on 2021-05-01 02:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210501_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='article',
            name='file',
            field=models.FileField(upload_to='code_files/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='article_img/', verbose_name='Заглавное изображение'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Заголовок'),
        ),
    ]
