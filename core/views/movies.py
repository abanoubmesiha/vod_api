from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import csv
import json

from .utils import envelope
from ..models import Movie, Comment

def get_one(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        comments = Comment.objects.filter(movie__id=movie_id)

        serialized_movie = movie.serialize()
        serialized_movie['comments'] = [comment.serialize() for comment in comments]
        
        if request.user.is_authenticated is False:
            serialized_movie['cdn_video'] = '401 Unauthorized'
            
        return JsonResponse(envelope(serialized_movie))
    except Movie.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movie_video(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return JsonResponse(envelope({
            'cdn_video': movie.cdn_video,
        }))
    except Movie.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))

@api_view(['GET'])
def add_movies_from_csv(request):
    try:
        moviesCdnOutput = open('core/movies-CdnOutput.csv', encoding="utf8")
        csv_movies_links = csv.reader(moviesCdnOutput)
        
        updated_movies = []
        created_movies = []
        for row in csv_movies_links:
            try:
                movie_file_name = row[1]
                movie_cdn_id = row[3]

                target_movie, created = Movie.objects.get_or_create(
                    video="FTPMovies/" + movie_file_name,
                    defaults={"title_ar": movie_file_name, "title_en": movie_cdn_id}
                )
                target_movie.cdn_video = "https://iframe.mediadelivery.net/embed/" + movie_cdn_id
                target_movie.save()
                if created is True:
                    created_movies.append({"id": target_movie.id, "title_en": target_movie.title_en})
                else:
                    updated_movies.append({"id": target_movie.id, "title_en": target_movie.title_en})
            except Exception as e:
                pass

        return JsonResponse(envelope(None, 200, {"updated_movies": json.dumps(updated_movies),"created_movies": json.dumps(created_movies)}))
    except Exception as e:
        return JsonResponse(envelope(e, 404, 'Error!'))