from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import envelope
from ..models import Section

def get_all(request):
    sections = Section.objects.all()
    data = [section.serialize() for section in sections]
    return JsonResponse(envelope(data))

@csrf_exempt
def test_cors(request):
    sections = Section.objects.all()
    data = [section.serialize() for section in sections]
    response = JsonResponse(envelope(data))
    response["Access-Control-Allow-Origin"] = 'http://49.12.195.122:3000'
    response['Access-Control-Allow-Methods'] = '*'
    response['Access-Control-Allow-Headers'] = '*'
    return response