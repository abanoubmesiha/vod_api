from django.db import models

from core.models.utils import try_to_serialize

class Country(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f"{self.title_en}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,

            "created_at": self.created_at,
        }

class Section(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    movies = models.ManyToManyField('Movie')
    series = models.ManyToManyField('Series')

    def __str__(self):
        return f"{self.title_en}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,

            "created_at": self.created_at,

            "movies": [try_to_serialize(movie) for movie in self.movies.all()],
            "series": [try_to_serialize(series) for series in self.series.all()],
        }

class Genre(models.Model):
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
