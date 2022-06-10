from .models import Movie, Comment
from django import forms
from django.forms import ModelForm, TextInput


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'Title', 'Year', 'Type', 'Poster']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control', 'name': 'movie',
            'id': 'movie', 'placeholder': 'Введите название'
        })}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'})
        }