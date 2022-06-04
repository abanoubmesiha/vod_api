from django.http import JsonResponse

from .utils import envelope
from ..models import Season

def get_one(request, season_id):
    try:
        season = Season.objects.get(pk=season_id)
        return JsonResponse(envelope(season.serialize({'with_series': True})))
    except Season.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))
    