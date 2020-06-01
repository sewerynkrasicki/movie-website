from django.shortcuts import render
from .models import Movie, Profile, Genre
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

def fav_movie_list(request):
    movies = request.user.profile.fav_movies.all()
    return render(request, 'movie/movie_list.html', {'movies' : movies})

def movie_list(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    query = request.GET.get('q')
    if query:
        query = Movie.objects.filter(
            Q(title__icontains=query)
            )
        return render(request, 'movie/movie_list.html', {'movies': query, 'genres': genres})
    elif request.method == 'POST':
        selected_item = Movie.objects.filter(
            Q(genre__genre_name__icontains=request.POST.get('item_id'))
        )
        return render(request, 'movie/movie_list.html', {'movies': selected_item, 'genres': genres})
    return render(request, 'movie/movie_list.html', {'movies': movies, 'genres': genres})

def index(request):
    query = request.GET.get('q')
    if query:
        query = Movie.objects.filter(
            Q(title__icontains=query)
            )
        return render(request, 'movie/movie_list.html', {'movies': query})
    return render(request, 'movie/index.html', {})

def detail_view(request,id):
    about_movie = {}
    about_movie["movie"] = Movie.objects.get(movie_id = id)
    mv = Movie.objects.get(movie_id = id)
    if request.user is not None:
        if request.method == "POST" and mv not in request.user.profile.fav_movies.all():
            movie = Movie.objects.get(movie_id=id)
            user = User.objects.get(id=request.user.id)
            user.profile.fav_movies.add(movie)
            user.save()
        elif request.method == "POST":
            movie = Movie.objects.get(movie_id=id)
            user = User.objects.get(id=request.user.id)
            user.profile.fav_movies.remove(movie)
            user.save()

    return render(request, "movie/detail_view.html", about_movie)

