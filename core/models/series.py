from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models.utils import try_to_serialize

def upload_to(instance, filename):
    return 'series/' + instance.title_en + '/' + filename

class Series(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    description_ar = models.CharField(max_length=5000, null=True, blank=True)
    description_en = models.CharField(max_length=5000, null=True, blank=True)
    
    cover = models.ImageField(upload_to=upload_to, default="default.gif", null=True, blank=True)
    poster = models.ImageField(upload_to=upload_to, default="default.gif", null=True, blank=True)
    trailer = models.CharField(max_length=300, null=True, blank=True)
    
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    releaseYear = models.IntegerField(default=1888, validators=[MaxValueValidator(2999), MinValueValidator(1888)])
    duration = models.IntegerField(default=0, validators=[MaxValueValidator(21840), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    seasons = models.ManyToManyField('Series', blank=True)
    genres = models.ManyToManyField('Genre', blank=True)
    
    director = models.ForeignKey('Director', null=True, blank=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField('Actor', blank=True)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return f"{self.title_en}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,

            "description_ar": self.description_ar,
            "description_en": self.description_en,

            "cover": self.cover.url,
            "poster": self.poster.url,
            "trailer": self.trailer,

            "rating": self.rating,
            "releaseYear": self.releaseYear,
            "duration": self.duration,
            "created_at": self.created_at,
            
            "country": try_to_serialize(self.country),
            "seasons":  [series.id if options.get('without_seasons') else try_to_serialize(series, {'without_seasons':True}) for series in self.seasons.all()],
            "genres": [try_to_serialize(genre) for genre in self.genres.all()],
            
            "director": try_to_serialize(self.director),
            "actors": [try_to_serialize(genre) for genre in self.actors.all()],
        }

def upload_episode_to(instance, filename):
    series = try_to_serialize(instance.series)
    series_title_en = series.get('title_en')
    return 'series/' + series_title_en + '/episodes/' + str(instance.number) + '/' + filename

class Episode(models.Model):
    number = models.IntegerField(default=1, validators=[MaxValueValidator(728), MinValueValidator(1)])
    
    cover = models.ImageField(upload_to=upload_episode_to, default="default.gif", null=True, blank=True)
    video = models.CharField(max_length=150, null=True, blank=True)

    series = models.ForeignKey('Series', on_delete=models.CASCADE)

    def __str__(self):
        series = try_to_serialize(self.series)
        return f"{series.get('title_en')} - E.{self.number}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "number": self.number,

            "cover": self.cover.url,
            "video": self.video,
            
            "series": try_to_serialize(self.series) if options.get('with_series') else self.series.id
        }
