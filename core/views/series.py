from django.http import JsonResponse

from .utils import envelope
from ..models import Series

def get_one(request, series_id):
    try:
        series = Series.objects.get(pk=series_id)
        return JsonResponse(envelope(series.serialize()))
    except Series.DoesNotExist:
        return JsonResponse(envelope(None, 404, 'Item Not Found'))
    