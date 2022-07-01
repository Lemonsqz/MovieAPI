import requests
from .forms import CommentForm
from django.shortcuts import render
from .models import Movie, Comment
from .forms import MovieForm
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import DetailView, CreateView
from .serializers import *
from django.urls import reverse_lazy


def index(request):
    apikey = '9d5fb454'
    url = 'https://www.omdbapi.com/?s={}&apikey=' + apikey
    form = MovieForm()
    try:

        if request.method == 'POST':
            form = MovieForm(request.POST)
            N = request.POST['name']
            print(request.POST['name'])  # тестовая запись POST

        res = requests.get(url.format(str(request.POST['name']))).json()
        if str(request.POST['name']).lower() not in str(Movie.objects.values_list('name')).lower():  # чекаем чтоб небыло дубляжа
            if res['Response'] == 'True':
                for i in res['Search']:
                    if i['Title'] not in str(Movie.objects.values_list('Title')):
                        Movie.objects.create(
                            name=i['Title'], Title=i['Title'],
                            Year=i['Year'], Type=i['Type'], Poster=i['Poster'],
                            slug=i['imdbID']
                        )  # сохр в админке
                # form.save()  # сохр в админке

        form = MovieForm()  # сброс поля

        movies = Movie.objects.filter(name__icontains=str(N))

        # result =[]
        # for i in Movie.objects.value('name'):
        #     if str(N).lower() in str(i).lower():
        #         result.append(i['name'])

        # print(requests.get(url.format(str(request.POST['name']))).text)
        print(res['Search'])
        print('test')

        context = {
            'form': form,
            'movie_list': movies,
        }
    except Exception:
        context = {'form': form}

    return render(request, 'movie/index.html', context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_details.html'
    context_object_name = 'movies'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'movie/add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.movies_id = self.kwargs['pk']
        return super().form_valid(form)

