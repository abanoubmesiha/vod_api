from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .utils import envelope
from ..models import Episode

@api_view(['GET'])
def get_one(request, episode_id):
    try:
        episode = Episode.objects.get(pk=episode_id)
        series_episodes = Episode.objects.filter(series__id=episode.series.id)

        serialized_episode = episode.serialize({'with_series': True})
        serialized_series_episodes = [episode.serialize() for episode in series_episodes]

        serialized_episode['series_episodes'] = serialized_series_episodes
        if request.user.is_authenticated is False:
            serialized_episode['video'] = '401 Unauthorized';
        return JsonResponse(envelope(serialized_episode))
    except Episode.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_episode_video(request, episode_id):
    try:
        episode = Episode.objects.get(pk=episode_id)
        return JsonResponse(envelope({'video': episode.video}))
    except Episode.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))
    