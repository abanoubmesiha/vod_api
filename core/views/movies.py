from django.http import JsonResponse

from .utils import envelope
from ..models import Movie

def get_one(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return JsonResponse(envelope(movie.serialize()))
    except Movie.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))