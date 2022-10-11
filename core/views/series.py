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


# @api_view(['GET'])
def add_series_episodes(request, pk):
    try:
        series_episodes_data = []
        series_title = Series.objects.filter(
            pk=pk).values().first()['title_en']
        episode_number = ""
        csv_file = open('CdnOutput.csv', encoding="utf8")
        csvreader = csv.reader(csv_file)

        for row in csvreader:
            if row[0:1] == [series_title]:
                series_episodes_data.append(row[1:])

        for csv_episode in series_episodes_data:
            print(csv_episode[0], re.match(
                "^EPS \d{2}_1_1\.mp4$", csv_episode[0]))
            if re.match("A[0-9]+\.mp4$", csv_episode[0]):
                episode_number = csv_episode[0].split(".")[0][-2:]

            elif re.match("EPS\d{2}_Master\.mp4$", csv_episode[0]):
                episode_number = csv_episode[0].split("_")[0][-2:]

            elif re.match("[a-zA-Z_0-9-]+_Eps\d{2}\.mp4$", csv_episode[0]):
                episode_number = csv_episode[0].split("_")[-1].split(".")[
                    0][-2:]

            # EPS 28_1_1.mp4
            elif re.match("EPS \d{2}_1_1\.mp4$", csv_episode[0]):
                episode_number = csv_episode[0].split(" ")[1][:2]

            # EPS07_1_1.mp4
            elif re.match("EPS\d{2}_1_1\.mp4$", csv_episode[0]):
                episode_number = csv_episode[0].split("_")[0][-2:]

            elif re.match("[a-zA-Z0-9 ]+EPS\d{2}\.mp4$", csv_episode[0]):
                episode_number = csv_episode[0].split(" ")[-1].split(".")[
                    0][-2:]

            elif re.match("EPS-\d{2,3}_1_1\.mp4$", csv_episode[0]):
                episode_number = csv_episode[0].split("-")[
                    1].split("_")[0]
                    
            elif re.match("[0-9]+\.mp4$", csv_episode[0]):
                episode_number = csv_episode[0].split(".")[
                    0][-2:]

            video_id = csv_episode[2]
            video_id_plus_thumbnail = csv_episode[3]

            cdn_video_link = "https://video.bunnycdn.com/play/50219/" + video_id
            thumbnail_link = "https://vz-76b7c0fe-9e0.b-cdn.net/" + video_id_plus_thumbnail

            print(episode_number)
            try:
                new_episode = Episode(
                    number=episode_number,
                    series_id=pk,
                    cdn_video=cdn_video_link,
                    cdn_cover=thumbnail_link
                )
                new_episode.save()
            except:
                print("fail to save")

        series_episodes_data_final_length = Episode.objects.count()
        return JsonResponse(envelope(f"{series_episodes_data_final_length} episodes added", 200, f'{len(series_episodes_data)} episodes of {series_title} series were added/updated successfully'))
    except Exception as e:
        return JsonResponse(envelope(e, 404, 'Series Not Found'))


def add_series(request):
    series_titles_array = []
    series_titles = Series.objects.values_list('title_en', flat=True)
    series_titles_array = [*series_titles]

    csv_file = open(
        'CdnOutput.csv', encoding="utf8")
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        if row[0] not in series_titles_array:
            series_titles_array.append(row[0])
            new_series = Series(
                title_ar=row[0],
                title_en=row[0],
            )
            new_series.save()
        else:
            pass

    return JsonResponse(envelope(series_titles_array, 200, f"series added successfully"))
