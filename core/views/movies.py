from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import csv

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

@api_view(['GET'])
def add_movies_from_csv(request):
    try:
        movies1 = open('core/movies1.csv', encoding="utf-8-sig")
        moviesCdnOutput = open('core/movies-CdnOutput.csv', encoding="utf8")
        csv_movies_names = csv.reader(movies1)
        csv_movies_links = csv.reader(moviesCdnOutput)

        for row in csv_movies_names:
            movie_name = row[0]
            video_file_name = row[5]
            
            merged_data_movie = None

            row2_video_name = None
            row2_video_id = None
            # for row2 in csv_movies_links:
            #     try:
            #         row2_video_name = row2[1]
            #         if row2_video_name == video_file_name:
            #             row2_video_id = row2[3]
            #     except:
            #         pass
            
            print(row, video_file_name, row2_video_name, row2_video_id)

            # a_cdn_movie = list(movie for movie in csv_movies_links if movie[1] == video_file_name)[0]
            # print(csv_movies_links)


            # target_movie = Movie.objects.get_or_create(title_ar=movie_name)
            # target_movie.cdn_video = "https://video.bunnycdn.com/play/50219/" + video_id

        
        return JsonResponse(envelope(None, 200, 'Still Testing...'))
    except Exception as e:
        return JsonResponse(envelope(e, 404, 'Error!'))