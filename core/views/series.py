from django.http import JsonResponse
from rest_framework.decorators import api_view
from .utils import envelope
from ..models import Series, Episode, Comment
import csv
import re


def get_one(request, series_id):
    try:
        series = Series.objects.get(pk=series_id)
        episodes = Episode.objects.filter(series__id=series_id)
        comments = Comment.objects.filter(series__id=series_id)

        serialized_series = series.serialize()
        serialized_series['episodes'] = [episode.serialize()
                                         for episode in episodes]
        serialized_series['comments'] = [comment.serialize()
                                         for comment in comments]
        return JsonResponse(envelope(serialized_series))
    except Series.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))


@api_view(['GET'])
def add_series_episodes(request, pk):
    try:
        series_episodes_data = []
        series_title = Series.objects.filter(
            pk=pk).values().first()['title_en']
        episode_number = ""
        csv_file = open('core/CdnOutput.csv', encoding="utf8")
        csvreader = csv.reader(csv_file)

        for row in csvreader:
            if row[0:1] == [series_title]:
                series_episodes_data.append(row[1:])
        
        for csv_episode in series_episodes_data:
            if re.search("A[0-9]+\.mp4", csv_episode[0]):
                episode_number = csv_episode[0].split(".")[
                    0][-2:]
            elif re.search("[a-zA-Z_0-9-]+_Eps\d{2}\.mp4", csv_episode[0]):
                episode_number = csv_episode[0].split("_")[-1].split(".")[
                    0][-2:]
            elif re.search("EPS\d{2}_Master\.mp4", csv_episode[0]):
                episode_number = csv_episode[0].split("_")[
                    0][-2:]
            elif re.search("[a-zA-Z0-9 ]+EPS\d{2}\.mp4", csv_episode[0]):
                episode_number = csv_episode[0].split(" ")[-1].split(".")[
                    0][-2:]
            
            video_id = csv_episode[2]
            video_id_plus_thumbnail = csv_episode[3]
            
            cdn_video_link = "https://video.bunnycdn.com/play/50219/" + video_id
            thumbnail_link = "https://vz-76b7c0fe-9e0.b-cdn.net/" + video_id_plus_thumbnail

            try:
                target_episode = Episode.objects.get(series__id=pk, number=episode_number)
                target_episode.cdn_video=cdn_video_link
                target_episode.cdn_cover=thumbnail_link
                target_episode.save()
            except:
                new_episode = Episode(
                    number=episode_number,
                    series_id=pk,
                    cdn_video=cdn_video_link,
                    cdn_cover=thumbnail_link
                )
                new_episode.save()

        return JsonResponse(envelope(None, 200, f'{len(series_episodes_data)} episodes of {series_title} series were added/updated successfully'))
    except Exception as e:
        return JsonResponse(envelope(e, 404, 'Series Not Found'))
