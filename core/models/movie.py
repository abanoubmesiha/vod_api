from django.contrib import admin
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models.utils import try_to_serialize

def upload_to(instance, filename):
    return 'movies/' + instance.title_en + '/' + filename

class Movie(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    description_ar = models.CharField(max_length=5000, null=True, blank=True)
    description_en = models.CharField(max_length=5000, null=True, blank=True)
    
    streaming_server = models.ForeignKey('Streaming_Server', default=1, null=True, blank=True, on_delete=models.SET_NULL)
    cover = models.ImageField(upload_to=upload_to, default="logo2.png", null=True, blank=True)
    poster = models.ImageField(upload_to=upload_to, default="logo2.png", null=True, blank=True)
    trailer = models.CharField(max_length=150, null=True, blank=True)
    video = models.CharField(max_length=150, null=True, blank=True)
    video_medium_q = models.CharField(max_length=150, null=True, blank=True)
    video_low_q = models.CharField(max_length=150, null=True, blank=True)
    cdn_video = models.CharField(max_length=150, null=True, blank=True)
    
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    release_year = models.IntegerField(default=1888, validators=[MaxValueValidator(2999), MinValueValidator(1888)])
    duration = models.IntegerField(default=0, validators=[MaxValueValidator(5160), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre', blank=True)
    
    director = models.ForeignKey('Director', null=True, blank=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField('Actor', blank=True)

    def __str__(self):
        return f"{self.title_ar}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,

            "description_ar": self.description_ar,
            "description_en": self.description_en,

            "streaming_server": self.streaming_server.url if self.streaming_server is not None else '',
            "cover": self.cover.url,
            "poster": self.poster.url,
            "trailer": self.trailer,
            "video": self.video,
            "video_medium_q": self.video_medium_q,
            "video_low_q": self.video_low_q,
            "cdn_video": self.cdn_video,

            "type": 'movies',
            "rating": self.rating,
            "release_year": self.release_year,
            "duration": self.duration,
            "created_at": self.created_at,
            
            "country": try_to_serialize(self.country),
            "genres": [try_to_serialize(genre) for genre in self.genres.all()],
            
            "director": try_to_serialize(self.director),
            "actors": [try_to_serialize(genre) for genre in self.actors.all()],
        }

class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title_ar']
    autocomplete_fields = ['director', 'actors']
