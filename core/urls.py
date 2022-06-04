from django.urls import path
from .views import sections
from .views import movies
from .views import series
from .views import seasons

urlpatterns = [
    path('sections', sections.get_all),
    path('movies/<int:movie_id>', movies.get_one),
    path('series/<int:series_id>', series.get_one),
    path('seasons/<int:season_id>', seasons.get_one),
]
