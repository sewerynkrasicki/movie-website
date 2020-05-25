from django.db import models

# Create your models here.


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.country_name

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.genre_name

class Director(models.Model):
    director_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    second_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.first_name + ' ' + self.second_name

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(default='', null=False)
    year = models.CharField(max_length=4, null=False)
    length = models.CharField(max_length=5, null=False)
    poster = models.URLField(default='', null=False)
    trailer = models.URLField(default='', null=False)
    rate = models.IntegerField(default=0, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    publisher_country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
