from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('movie', views.movie_list, name="movie_list"),
    path('movie/fav', views.fav_movie_list, name="fav_movie_list"),
    path('detail/<id>', views.detail_view, name="detail"),
    path('detail/<id>/<user_id>', views.detail_view, name="fav")
]