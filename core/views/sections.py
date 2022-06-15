from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import envelope
from ..models import Section

def get_all(request):
    sections = Section.objects.all()
    data = [section.serialize() for section in sections]
    return JsonResponse(envelope(data))