from django.urls import path, include
from .views import *

app_name = 'search'
urlpatterns = [
    path('', ESearchView.as_view(), name='index'),
]