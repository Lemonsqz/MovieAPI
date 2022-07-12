from .models import Movie, Comment, UserMovieRating, RatingStar
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


class RatingForm(forms.ModelForm):
    # Форма добавления рейтинга
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = UserMovieRating
        fields = ("star",)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
