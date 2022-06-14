from django.http import JsonResponse

from .utils import envelope
from ..models import Section

def get_all(request):
    sections = Section.objects.all()
    data = [section.serialize() for section in sections]
    return JsonResponse(envelope(data))

def test_cors(request):
    sections = Section.objects.all()
    data = [section.serialize() for section in sections]
    response = JsonResponse(envelope(data))
    response["Access-Control-Allow-Origin"] = 'http://49.12.195.122:3000'
    response['Access-Control-Allow-Methods'] = 'POST,GET,OPTIONS,PUT,DELETE'
    response['Access-Control-Allow-Headers'] = 'Content-Type,Accept'
    return response