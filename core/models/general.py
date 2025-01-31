from django.contrib import admin
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models.utils import try_to_serialize

class Country(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f"{self.title_ar}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,
        }

class Section(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    order = models.IntegerField(default=20, validators=[MaxValueValidator(20), MinValueValidator(1)])
    
    movies = models.ManyToManyField('Movie', blank=True)
    series = models.ManyToManyField('Series', blank=True)

    def __str__(self):
        return f"{self.title_ar} ({self.order})"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,

            "created_at": self.created_at,
            
            "order": self.order,

            "movies": [try_to_serialize(movie) for movie in self.movies.all()],
            "series": [try_to_serialize(series) for series in self.series.all()],
        }

class SectionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['movies', 'series']

class Genre(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.title_ar}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,
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

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['movie__title_ar', 'series__title_ar', 'episode__number']