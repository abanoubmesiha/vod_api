from django.urls import path
from .views import sections
from .views import movies

urlpatterns = [
    path('sections', sections.get_all),
    path('movies/<int:movie_id>', movies.get_one),
]
