from django.shortcuts import render
from .models import Movie
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    query = request.GET.get('q')
    if query:
        query = Movie.objects.filter(
            Q(title__icontains=query) |
            Q(genre__genre_name__icontains=query) |
            Q(director__first_name__icontains=query) |
            Q(director__second_name__icontains=query)
            )
        if query:
            return render(request, 'movie/movie_list.html', {'movies': query})
        return render(request, 'movie/movie_list.html', {'movies': movies})
    return render(request, 'movie/movie_list.html', {'movies': movies})

def index(request):
    query = request.GET.get('q')
    if query:
        query = Movie.objects.filter(
            Q(title__icontains=query) |
            Q(genre__genre_name__icontains=query) |
            Q(director__first_name__icontains=query) |
            Q(director__second_name__icontains=query)
            )
        return render(request, 'movie/movie_list.html', {'movies': query})
        
    return render(request, 'movie/index.html', {})

def detail_view(request, id):
    query = request.GET.get('q')
    if query:
        query = Movie.objects.filter(
            Q(title__icontains=query) |
            Q(genre__genre_name__icontains=query) |
            Q(director__first_name__icontains=query) |
            Q(director__second_name__icontains=query)
            )
        return render(request, 'movie/movie_list.html', {'movies': query})
    about_movie = {}
    about_movie["movie"] = Movie.objects.get(movie_id = id)

    return render(request, "movie/detail_view.html", about_movie)
