import requests
from django.shortcuts import render
from .models import Movie
from .forms import MovieForm
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import DetailView


def index(request):
    apikey = '9d5fb454'
    url = 'https://www.omdbapi.com/?s={}&apikey=' + apikey
    form = MovieForm()
    try:
        if request.method == 'POST':
            form = MovieForm(request.POST)
            print(request.POST['name'])  # тестовая запись POST

        res = requests.get(url.format(str(request.POST['name']))).json()
        if str(request.POST['name']) not in str(Movie.objects.values_list('name')):  # чекаем чтоб небыло дубляжа
            if res['Response'] == 'True':
                form.save()  # сохр в админке

        form = MovieForm()  # сброс поля

        movies = Movie.objects.all()

        all_movies = []

        if res['Response'] == 'True':
            film_info = {
                'title': res['Search'][0]['Title'],
                'year': res['Search'][0]['Year'],
                # 'plot': res['Search'][0]['Plot'],
                'poster': res['Search'][0]['Poster'],

                'response': res['Response']

            }

            all_movies.append(film_info)
        print(requests.get(url.format(str(request.POST['name']))).text)
        context = {
            'all_info': all_movies,
            'form': form,
            'movie_list': movies,
        }
    except MultiValueDictKeyError:
        context = {'form': form}

    return render(request, 'movie/index.html', context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_details.html'
    context_object_name = 'movies'
    slug_url_kwarg = 'slug'
