from django.db import models

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