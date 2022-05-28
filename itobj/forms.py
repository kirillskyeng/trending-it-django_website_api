from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category not selected'

    class Meta:
        model = ItObject
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content', 'cols': 60, 'rows': 10}),
            'is_published': forms.CheckboxInput(),
            'cat': forms.Select(attrs={'class': 'form-control'})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
