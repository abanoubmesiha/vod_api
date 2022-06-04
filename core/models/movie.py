from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models.utils import try_to_serialize

class Movie(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    description_ar = models.CharField(max_length=5000, null=True, blank=True)
    description_en = models.CharField(max_length=5000, null=True, blank=True)
    
    cover = models.CharField(max_length=300, null=True, blank=True)
    poster = models.CharField(max_length=300, null=True, blank=True)
    trailer = models.CharField(max_length=300, null=True, blank=True)
    
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    releaseYear = models.IntegerField(default=1888, validators=[MaxValueValidator(2999), MinValueValidator(1888)])
    duration = models.IntegerField(default=0, validators=[MaxValueValidator(5160), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)

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
        }

