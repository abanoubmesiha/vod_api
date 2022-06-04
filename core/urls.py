from django.urls import path
from .views import sections
from .views import movies
from .views import series

urlpatterns = [
    path('sections', sections.get_all),
    path('movies/<int:movie_id>', movies.get_one),
    path('series/<int:series_id>', series.get_one),
]
