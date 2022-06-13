from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import sections
from .views import movies
from .views import series
from .views import episodes
from .views import auth

urlpatterns = [
    path('login/', auth.login),
    path('api-token-auth', auth.get_token),
    path('api-token-auth2', obtain_auth_token),
    path('sections', sections.get_all),
    path('movies/<int:movie_id>', movies.get_one),
    path('movies/<int:movie_id>/video', movies.get_movie_video),
    path('series/<int:series_id>', series.get_one),
    path('episodes/<int:episode_id>', episodes.get_one),
    path('episodes/<int:episode_id>/video', episodes.get_episode_video),
]
