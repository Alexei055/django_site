# импорт всех необходимых классов и функций
import json
from django.contrib import auth
from django.http import HttpResponse
from django.views import View
from .models import BookmarkArticle


class BookmarkView(View):
    # в данную переменную будет устанавливаться модель закладок, которую необходимо обработать
    model = BookmarkArticle

    def post(self, request, pk):
        # если пользователь не авторизирован
        if not request.user.is_authenticated:
            # то возвращаем ответ, что он не авторизирован
            return HttpResponse(
                json.dumps({"user_login": 0}),
                content_type="application/json"
            )
        # получение объекта пользователя
        user = auth.get_user(request)
        # пытаемся получить закладку из таблицы, или создать новую
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        # если не была создана новая закладка,
        # то считаем, что запрос был на удаление закладки
        if not created:
            bookmark.delete()

        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(obj_id=pk).count(),
                "user_mark": self.model.objects.filter(user=user).count()
            }),
            content_type="application/json"
        )
