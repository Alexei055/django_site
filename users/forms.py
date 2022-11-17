from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm


class UserRegisterForm(UserCreationForm):
    # объявление поля для ввода имени пользователя
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Имя пользователя'}),
                               help_text='Имя пользователя должно содержать только буквы, цифры и символы @/./+/-/_')
    # объявление поля для ввода пароля
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                  'style': 'margin-top:24px;'}),
                                help_text='Пароль должен содержать минимум 8 символов и не может состоять '
                                          'только из цифр')
    # поле для ввода подтверждения пароля
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Подтверждение пароля',
                                           'style': 'margin-top:48px'}))
    # поле для ввода почты пользователя
    email = forms.EmailField(label='Почта',
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'E-Mail', 'style': 'margin-top:32px;'}))

    class Meta:
        # указание на модель пользователя
        model = User
        # какие поля формы будут отображаться на странице
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['image']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='',
                                   widget=forms.PasswordInput(attrs={'class': 'form-group-secondary',
                                                                     'type': 'password',
                                                                     'placeholder': 'Старый пароль'}))
    # поле для ввода нового пароля
    new_password1 = forms.CharField(label='', max_length=30,
                                    widget=forms.PasswordInput(attrs={'class': 'form-group-secondary',
                                                                      'type': 'password',
                                                                      'placeholder': 'Новый пароль'}),
                                    help_text='Пароль должен содержать минимум 8 символов и не может состоять '
                                              'только из цифр')
    new_password2 = forms.CharField(label='',
                                    max_length=30,
                                    widget=forms.PasswordInput(attrs={'class': 'form-group-secondary',
                                                                      'type': 'password',
                                                                      'placeholder': 'Подтверждение нового пароля'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='', max_length=30,
                                    widget=forms.PasswordInput(attrs={'class': 'form-group-secondary', 'type': 'password','placeholder': 'Новый пароль'}),
                                    help_text='Пароль должен содержать минимум 8 символов и не может состоять '
                                              'только из цифр')
    new_password2 = forms.CharField(label='',
                                    max_length=30,
                                    widget=forms.PasswordInput(attrs={'class': 'form-group-secondary', 'type': 'password',
                                                                      'placeholder': 'Подтверждение нового пароля'}))

    class Meta:
        fields = ('new_password1', 'new_password2')


class EmailValidationOnForgotPassword(PasswordResetForm):
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-group-secondary', 'placeholder': 'Адрес электронной почты'}))

    class Meta:
        fields = 'email'

    def clean_email(self):
        email = self.cleaned_data['email']

        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "Пользователя с такой почтой не существует"
            self.add_error('email', msg)
        return email
