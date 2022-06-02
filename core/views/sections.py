from django.http import HttpResponse
from ..models import Section

def get_all(request):
    return HttpResponse('hi')