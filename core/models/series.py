from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models.utils import try_to_serialize

class Series(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    description_ar = models.CharField(max_length=5000, null=True, blank=True)
    description_en = models.CharField(max_length=5000, null=True, blank=True)
    
    cover = models.CharField(max_length=300, null=True, blank=True)
    poster = models.CharField(max_length=300, null=True, blank=True)
    trailer = models.CharField(max_length=300, null=True, blank=True)
    
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    releaseYear = models.IntegerField(default=1888, validators=[MaxValueValidator(2999), MinValueValidator(1888)])
    duration = models.IntegerField(default=0, validators=[MaxValueValidator(21840), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    seasons = models.ManyToManyField('Series', null=True, blank=True)
    genre = models.ManyToManyField('Genre', null=True, blank=True)

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

            "cover": self.cover,
            "poster": self.poster,
            "trailer": self.trailer,

            "rating": self.rating,
            "releaseYear": self.releaseYear,
            "duration": self.duration,
            "created_at": self.created_at,
            
            "country": try_to_serialize(self.country),
            "seasons":  [series.id if options.get('without_seasons') else try_to_serialize(series, {'without_seasons':True}) for series in self.seasons.all()],
            "genre": try_to_serialize(self.genre),
        }

class Episode(models.Model):
    number = models.IntegerField(default=1, validators=[MaxValueValidator(728), MinValueValidator(1)])
    
    cover = models.CharField(max_length=300, null=True, blank=True)

    series = models.ForeignKey('Series', on_delete=models.CASCADE)

    def __str__(self):
        series = try_to_serialize(self.series)
        return f"{series.get('title_en')} - E.{self.number}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "number": self.number,

            "cover": self.cover,
            
            "series": try_to_serialize(self.series) if options.get('with_series') else self.series.id
        }
