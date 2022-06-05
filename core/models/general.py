from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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

class Comment(models.Model):
    body = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    up_votes = models.IntegerField(default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    down_votes = models.IntegerField(default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])

    # user = models.ForeignKey('User', on_delete=models.SET_NULL)
    movie = models.ForeignKey('Movie', null=True, blank=True, on_delete=models.CASCADE)
    series = models.ForeignKey('Series', null=True, blank=True, on_delete=models.CASCADE)
    episode = models.ForeignKey('Episode', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.body}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "body": self.body,

            "created_at": self.created_at,

            "up_votes": self.up_votes,
            "down_votes": self.down_votes,

            "user": None,# try_to_serialize(self.user),
        }
