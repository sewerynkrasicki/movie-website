from django.db import models

# Create your models here.


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=50, null=False)

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=50, null=False)

class Director(models.Model):
    director_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    second_name = models.CharField(max_length=50, null=False)

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    year = models.CharField(max_length=4, null=False)
    length = models.CharField(max_length=5, null=False)
    poster = models.URLField(default='')
    trailer = models.URLField(default='')
    rate = models.IntegerField(default=0, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    publisher_country = models.ForeignKey(Country, on_delete=models.PROTECT)
