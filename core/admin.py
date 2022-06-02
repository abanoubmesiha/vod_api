from django.contrib import admin
from .models import (
    Movie, Country, Series, Episode
)


admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Series)
admin.site.register(Episode)