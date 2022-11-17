from main.models import Article

def article_count(request):
    return {'article_count': Article.objects.all()}