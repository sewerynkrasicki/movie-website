from django.shortcuts import render

# Create your views here.

def movie_list(request):
    return render(request, 'movie/movie_list.html', {})

def index(request):
    return render(request, 'movie/index.html', {})

