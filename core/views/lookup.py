from django.http import JsonResponse

from .utils import envelope
from ..models import Genre

def get_genres(request):
    genres = Genre.objects.all()
    data = [genre.serialize() for genre in genres]
    return JsonResponse(envelope(data))