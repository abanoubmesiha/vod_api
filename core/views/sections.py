from django.http import JsonResponse

from .utils import envelope
from ..models import Section

def get_all():
    sections = Section.objects.all()
    data = [section.serialize() for section in sections]
    return JsonResponse(envelope(data))