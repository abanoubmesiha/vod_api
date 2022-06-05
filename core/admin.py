from django.contrib import admin
from .models import (
    Movie, Country, Series, Episode, Section, Artist, Actor, Director,
    Genre
)


admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Series)
admin.site.register(Episode)
admin.site.register(Section)
admin.site.register(Artist)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)