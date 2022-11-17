from django import template
from django.template.defaultfilters import stringfilter
import re
from main.models import ArticleStatistic
from django.db.models import Sum
from django.utils import timezone
register = template.Library()


@register.filter(name='nbsp2space', is_safe=True)
@stringfilter
def nbsp2space(value):
    return re.sub('&nbsp;', ' ', value, flags=re.IGNORECASE)


# вывод статей по количеству просмотров за 7 дней
@register.simple_tag
def get_popular_articles_for_week():
    popular = ArticleStatistic.objects.filter(
        date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]).values('id',
                                                                                     'article__title',
                                                                                     'article__content').annotate(
        views=Sum('views')).order_by(
        '-views')[:3]
    return popular


@register.filter
def user_in(Article, user):
    if user.is_authenticated:
        return Article.filter(user=user).exists()
    return False
