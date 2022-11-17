from django.urls import path
from .views import *

urlpatterns = [
    path('api/article/<int:pk>/bookmark/',
         BookmarkView.as_view(),
         name='article_bookmark')
]
