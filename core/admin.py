from django.contrib import admin
from .models import (
    Movie, Country, Series, Season, Episode, Section
)


admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Series)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Section)