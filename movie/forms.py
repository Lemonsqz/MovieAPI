from .models import Movie
from django.forms import ModelForm, TextInput


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control', 'name': 'movie',
            'id': 'movie', 'placeholder': 'Введите название'
        })}