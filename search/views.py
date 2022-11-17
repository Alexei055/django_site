from django.shortcuts import render
from django.views import View
from main.models import Article


class ESearchView(View):
    # название и путь до шаблона
    template_name = 'search/search.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # получение параметра поиска
        question = request.GET.get('q')
        if question is not None:
            # поиск по статьям
            search_articles = Article.objects.filter(content__search=question)
            context['article_lists'] = search_articles
        return render(request, template_name=self.template_name, context=context)
