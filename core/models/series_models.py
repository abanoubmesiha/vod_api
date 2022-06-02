from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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

    def __str__(self):
        return f"{self.title_en}"

    def serialize(self):
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
            
            "country": self.country.serialize(),
        }

class Episode(models.Model):
    no = models.IntegerField(default=1, validators=[MaxValueValidator(728), MinValueValidator(1)])
    
    cover = models.CharField(max_length=300, null=True, blank=True)

    series = models.ForeignKey('Series', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.no}"

    def serialize(self):
        return {
            "id": self.id,

            "no": self.no,

            "cover": self.cover,
            
            "series": self.series.serialize(),
        }
