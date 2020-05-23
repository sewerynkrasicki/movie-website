from django.contrib import admin
from .models import Country
from .models import Director
from .models import Genre
from .models import Movie

# Register your models here.

admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)