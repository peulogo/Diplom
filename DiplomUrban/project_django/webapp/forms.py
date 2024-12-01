from django import forms
from .models import Entry
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'user_input',
                'name': 'user_input',
                'required': True,
                'placeholder': 'Введите ваш текст',
            })
        }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
