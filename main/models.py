from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import os
from django.contrib.contenttypes.fields import GenericRelation, ContentType
from django_cleanup import cleanup
from comment.models import Comment
from like_system.models import LikeSystem
from ckeditor_uploader.fields import RichTextUploadingField
from djangosite.settings import BASE_DIR


@cleanup.ignore
class Article(models.Model):
    CHOICES = [("site_img/"+i, i.split('.webp')[0]) for i in os.listdir(path=os.path.join(BASE_DIR, 'media/site_img'))]
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Контент')
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='code_files/', verbose_name='Файл', null=True, blank=True)
    image = models.ImageField(choices=CHOICES, verbose_name='Заглавное изображение')
    comments = GenericRelation(Comment)
    likesystem = GenericRelation(LikeSystem, related_query_name="likes_target")

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.file.name)

    def get_absolute_url(self):
        return reverse('articles-detail', kwargs={'pk': self.pk})

    def get_bookmark_count(self):
        return self.bookmarkarticle_set.all().count()


class ArticleStatistic(models.Model):
    class Meta:
        db_table = "ArticleStatistic"  # название даблицы

    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # внешний ключ на статью
    date = models.DateField('Дата', default=timezone.now)  # дата
    views = models.IntegerField('Просмотры', default=0)  # количество просмотров в эту дату

    def __str__(self):
        return self.article.title


class ArticleStatisticAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')  # отображаемые поля в админке
    search_fields = ('__str__',)  # поле по которому производится поиск
