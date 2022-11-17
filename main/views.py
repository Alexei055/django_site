import re
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.views.generic import ListView, UpdateView, CreateView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


class PostListViews(ListView):
    model = Article  # модель статей
    template_name = 'main/home.html'  # название шаблона
    context_object_name = 'articles'  # имя переменной к которой следует обращаться при заполнении шаблона
    ordering = ["pub_date"]


class CreateArticleView(CreateView):
    form_class = ArticleForm
    template_name = 'main/create_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        true_content = re.sub('<pre>', '<pre class="lang-python3 py3">', form.instance.content, flags=re.IGNORECASE)
        form.instance.content = true_content
        return super().form_valid(form)


class UpdateArticleView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'main/update_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        true_content = re.sub('<pre>', '<pre class="lang-python3 py3">', form.instance.content, flags=re.IGNORECASE)
        form.instance.content = true_content
        return super().form_valid(form)


def post_detail(request, pk):
    template_name = 'main/article_detail.html'  # название шаблона
    post = get_object_or_404(Article, pk=pk)  # получение статьи из модели
    context = {}

    # забираем объект сегодняшней статистики или создаём новый, если требуется
    obj, created = ArticleStatistic.objects.get_or_create(
        defaults={
            "article": post,
            "date": timezone.now()
        },
        date=timezone.now(), article=post)
    obj.views += 1  # инкрементируем счётчик просмотров и обновляем поле в базе данных
    obj.save(update_fields=['views'])

    popular = ArticleStatistic.objects.filter(
        date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]).values('article__title',
                                                                                     'article__id').annotate(
        views=Sum('views')).order_by('-views')[:3]

    context['popular_list'] = popular  # Добавим в контекст список статей
    context['post'] = post
    # отправка на шаблон необходимых данных для генерации шаблона
    return render(request, template_name, context)


# функция для скачивания файла из статьи
def download(request, pk):
    file = get_object_or_404(Article, pk=pk).file  # получаем файл из статьи
    response = HttpResponse(open(f"{file.path}", 'rb').read())  # открываем файл и начинаем
    # формировать ответ для пользователя
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = f"attachment; filename={file.name[11:]}"
    return response


@login_required(login_url='login')
def post_favourite_list(request):
    user = request.user
    favourite_posts = [i.obj for i in user.bookmarkarticle_set.all()]
    context = {
        'favourite_posts': favourite_posts
    }
    return render(request, 'main/article_favourite_list.html', context)
