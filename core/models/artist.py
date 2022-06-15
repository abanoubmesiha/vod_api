from django.db import models

from core.models.utils import try_to_serialize

class Artist(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title_en}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,

            "created_at": self.created_at,
        }

class Actor(Artist):
    pass

class Director(Artist):
    pass

class Cast(models.Model):
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE, primary_key=True)

    actors = models.ManyToManyField('Actor', blank=True)
    directors = models.ManyToManyField('Director', blank=True)

    def __str__(self):
        return f"{self.movie.title_en} Cast"

    def serialize(self, options={}):
        return {
            "actors": [try_to_serialize(actor) for actor in self.actors.all()],
            "directors": [try_to_serialize(director) for director in self.directors.all()],
        }