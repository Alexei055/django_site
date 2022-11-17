from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        # пытаемся сохранить изменения в существуюем профиле
        instance.profile.save()
    except ObjectDoesNotExist:
        # если не получается, то создаем новую запись профиля пользователя
        Profile.objects.create(user=instance)
