from django.http import JsonResponse

from .utils import envelope
from ..models import Season

def get_one(request, season_id):
    try:
        season = Season.objects.get(pk=season_id)
        other_seasons = Season.objects.filter(series__id=season.series.id)
        serialized_season = season.serialize({'with_series': True})
        serialized_season['series']['seasons'] = [s.serialize() for s in other_seasons]
        return JsonResponse(envelope(serialized_season))
    except Season.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))
    