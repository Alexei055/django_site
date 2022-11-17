from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import *
from .backends import *


# функция регистрации пользователя
def register(request):
    # проверка на метод сообщения из формы
    if request.method == 'POST':
        # заполнение формы после получения данных
        form = UserRegisterForm(request.POST)
        # проверка на правильное заполнение формы
        if form.is_valid():
            # сохранение данных формы в базе данных
            user = form.save()
            # авторизация пользователя
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # перенаправление пользователя на главную страницу по пути из приложения main
            return redirect('articles')
    # если проверка на метод не прошла, то генерируется пустая форма
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form": form})


# функция входа пользователя в свой аккаунт
def user_login(request):
    # проверка на медот
    if request.method == 'POST':
        # заполнение формы
        form = UserLoginForm(data=request.POST)
        # проверка на правильное заполение формы
        if form.is_valid():
            # получение профиля пользователя из формы
            user = form.get_user()
            # авторизация пользователя
            login(request, user)
            # перенаправление пользователя на главную страницу по пути из приложения main
            return redirect('articles')
    # если проверка на метод не прошла, то генерируется пустая форма
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {"form": form})


# функция выхода пользователя из своего аккаунта
def user_logout(request):
    # разлогиниваем пользователя
    logout(request)
    # перенаправляем пользователя на страницу входа
    return redirect('login')


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid or p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, 'Успешно!')
            return redirect('profile')
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def profile_detail(request, pk):
    profile = get_object_or_404(User, pk=pk)
    return render(request, 'users/profile_detail.html', {'profile': profile})