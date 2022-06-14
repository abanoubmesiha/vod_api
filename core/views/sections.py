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
    response["access-control-allow-origin"] = 'http://49.12.195.122:3000'
    response['access-control-allow-methods'] = 'GET, PUT, POST, DELETE, HEAD, OPTIONS'
    # response['access-control-allow-headers'] = 'Content-Type'
    response['Content-Type'] = 'application/json'
    return response