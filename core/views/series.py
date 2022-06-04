from django.http import JsonResponse

from .utils import envelope
from ..models import Series, Episode

def get_one(request, series_id):
    try:
        series = Series.objects.get(pk=series_id)
        episodes = Episode.objects.filter(series__id=series_id)

        serialized_series = series.serialize()
        serialized_series['episodes'] = [episode.serialize() for episode in episodes]
        return JsonResponse(envelope(serialized_series))
    except Series.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))
    