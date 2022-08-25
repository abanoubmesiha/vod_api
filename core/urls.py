from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from .views import auth
from .views import catalog
from .views import episodes
from .views import lookup
from .views import movies
from .views import sections
from .views import series

urlpatterns = [
    path('login/', auth.login),
    path('api-token-auth/', csrf_exempt(obtain_auth_token)),
    path('sections', sections.get_all),
    path('movies/<int:movie_id>', movies.get_one),
    path('movies/<int:movie_id>/video', movies.get_movie_video),
    path('series/<int:series_id>', series.get_one),
    path('episodes/<int:episode_id>', episodes.get_one),
    path('episodes/<int:episode_id>/video', episodes.get_episode_video),
    path('catalogs', catalog.get),
    path('lookup/genres', lookup.get_genres),
    path('series/<int:pk>/eps', series.add_series_episodes)
]
