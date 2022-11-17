from django.urls import path
from .views import *
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('', PostListViews.as_view(), name='articles'),
    path('article/<int:pk>/', post_detail, name='articles-detail'),
    path('download/<int:pk>/', download, name='articles-download'),
    path('favourites/', post_favourite_list, name='post_favourite_list'),
    path('create_article/', staff_member_required(CreateArticleView.as_view()), name='create_article'),
    path('edit_article/<int:pk>/', staff_member_required(UpdateArticleView.as_view()), name='edit_article'),
]
