from django.contrib import admin
from .models import (
    Movie, MovieAdmin,
    Country,
    Series, SeriesAdmin,
    Section, SectionAdmin,
    Artist, ArtistAdmin,
    Actor, ActorAdmin,
    Director, DirectorAdmin,
    Genre,
    Comment, CommentAdmin
)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Country)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre)
admin.site.register(Comment, CommentAdmin)