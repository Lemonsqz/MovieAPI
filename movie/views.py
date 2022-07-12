import requests
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .models import Movie, Comment, UserMovieRating
from .forms import MovieForm, RatingForm
from django.views.generic import DetailView, CreateView
from .serializers import *
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect


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
        if str(request.POST['name']).lower() not in str(
                Movie.objects.values_list('name')).lower():  # чекаем чтоб небыло дубляжа
            if res['Response'] == 'True':
                for i in res['Search']:
                    if i['Title'] not in str(Movie.objects.values_list('Title')):
                        Movie.objects.create(
                            name=i['Title'], Title=i['Title'],
                            Year=i['Year'], Type=i['Type'], Poster=i['Poster']

                        )  # сохр в админке
                # form.save()  # сохр в админке

        form = MovieForm()  # сброс поля

        movies = Movie.objects.filter(name__icontains=str(N))

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["star_form"] = RatingForm()

        return context


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'movie/add_comment.html'

    # определяет текущий фильм
    def form_valid(self, form):
        form.instance.movie_id = self.kwargs['pk']
        return super().form_valid(form)


class AddStarRating(View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            UserMovieRating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


def favourite_add(request, id):
    movie = get_object_or_404(Movie, id=id)
    if movie.favourites.filter(id=request.user.id).exists():
        movie.favourites.remove(request.user)
    else:
        movie.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourite_list(request):
    new = Movie.objects.filter(favourites=request.user)
    return render(request, 'movie/favourites.html', {'new': new})
