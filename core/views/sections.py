from django.http import JsonResponse

from .utils import envelope
from ..models import Section

def get_all(request):
    sections = Section.objects.all().order_by('order')
    data = [section.serialize() for section in sections]
    return JsonResponse(envelope(data))