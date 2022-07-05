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
        
        if request.user.is_authenticated is False:
            serialized_movie['streaming_server'] = serialized_movie['video'] = serialized_movie['video_medium_q'] = serialized_movie['video_low_q'] = serialized_movie['cdn_video'] = '401 Unauthorized'
            
        return JsonResponse(envelope(serialized_movie))
    except Movie.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movie_video(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return JsonResponse(envelope({
            'streaming_server': movie.streaming_server.url if movie.streaming_server is not None else '',
            'video': movie.video,
            'video_medium_q': movie.video_medium_q,
            'video_low_q': movie.video_low_q,
            'cdn_video': movie.cdn_video,
        }))
    except Movie.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))