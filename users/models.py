from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils import timezone


class Profile(models.Model):
    # устанавливаем связь модели со стандартной моделью пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # поле для хранения аватарки пользователя
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # поле хранящее время последнего посещения
    last_online = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # функция обрезки загруженной аватарки пользоватля под формат
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # В данном методе проверяем, что дата последнего посещения не старше 15 минут
    def is_online(self):
        if self.last_online:
            return (timezone.now() - self.last_online) < timezone.timedelta(minutes=1)
        return False

    # Если пользователь посещал сайт не более 15 минут назад,
    def get_online_info(self):
        if self.is_online():
            # то возвращаем информацию, что он онлайн
            return 'Онлайн'
        if self.last_online:
            # иначе пишем сообщение о последнем посещении
            return _(f'Последнее посещение: {naturaltime(self.last_online)}')
            # если инфомации о посещении нет, вернём информацию,
            # что последнее посещение неизвестно
        else:
            return 'Не известно'

    # аналогичная функция из приложения main
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})
