from django.http import JsonResponse

from .utils import envelope
from ..models import Movie

def get_one(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return JsonResponse(envelope(movie.serialize()))