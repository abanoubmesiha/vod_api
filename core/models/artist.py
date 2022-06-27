from django.db import models

from core.models.utils import try_to_serialize

class Artist(models.Model):
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.title_en}"

    def serialize(self, options={}):
        return {
            "id": self.id,

            "title_ar": self.title_ar,
            "title_en": self.title_en,
        }

class Actor(Artist):
    pass

class Director(Artist):
    pass