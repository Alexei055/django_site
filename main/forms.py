from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'file', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-group-secondary', 'placeholder': 'Заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-group-secondary'})
        }
        labels = {
            'title': ''
        }
