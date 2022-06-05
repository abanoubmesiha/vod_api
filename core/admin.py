from django.contrib import admin
from .models import (
    Movie, Country, Series, Episode, Section
)


admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Series)
admin.site.register(Episode)
admin.site.register(Section)