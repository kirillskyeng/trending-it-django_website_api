from django import forms
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
