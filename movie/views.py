from django.shortcuts import render
from .models import Movie
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

def index(request):
    return render(request, 'movie/index.html', {})

def detail_view(request, id):
    about_movie = {}
    about_movie["movie"] = Movie.objects.get(movie_id = id)

    return render(request, "movie/detail_view.html", about_movie)