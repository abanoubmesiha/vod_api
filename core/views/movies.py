from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .utils import envelope
from ..models import Movie, Comment

def get_one(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        comments = Comment.objects.filter(movie__id=movie_id)

        serialized_movie = movie.serialize()
        serialized_movie['comments'] = [comment.serialize() for comment in comments]
        try:
            serialized_movie['cast'] = movie.cast.serialize()
        except:
            serialized_movie['cast'] = None
            
        return JsonResponse(envelope(serialized_movie))
    except Movie.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movie_video(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return JsonResponse(envelope({'video': movie.video}))
    except Movie.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))