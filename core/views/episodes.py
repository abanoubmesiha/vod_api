from django.http import JsonResponse

from .utils import envelope
from ..models import Episode

def get_one(request, episode_id):
    try:
        episode = Episode.objects.get(pk=episode_id)
        series_episodes = Episode.objects.filter(series__id=episode.series.id)

        serialized_episode = episode.serialize({'with_series': True})
        serialized_series_episodes = [episode.serialize() for episode in series_episodes]

        serialized_episode['series_episodes'] = serialized_series_episodes
        return JsonResponse(envelope(serialized_episode))
    except Episode.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))
    