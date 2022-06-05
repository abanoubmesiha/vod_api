from django.http import JsonResponse

from .utils import envelope
from ..models import Movie, Comment

def get_one(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        comments = Comment.objects.filter(movie__id=movie_id)

        serialized_movie = movie.serialize()
        serialized_movie['comments'] = [comment.serialize() for comment in comments]
        return JsonResponse(envelope(serialized_movie))
    except Movie.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))