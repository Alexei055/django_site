from django.contrib.auth.models import User
from django.db import models
from main.models import Article


# создаем родительский класс
class BookmarkBase(models.Model):
    class Meta:
        abstract = True

    # внешний ключь на объект пользователя
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# основная модель закладок
# дочерний класс класса BookmarkBase
class BookmarkArticle(BookmarkBase):
    class Meta:
        db_table = "bookmark_article"  # название таблицы

    # внешний ключь на статью
    obj = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE)
