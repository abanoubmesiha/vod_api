from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def login(request):
    content = {'message': 'Hello, World!'}
    return Response(content)

def get_token(request):
    response = Response('59475edec9930601664b5fa6a13b2464cc05130d')
    # response["access-control-allow-origin"] = 'http://49.12.195.122:8000'
    response['access-control-allow-methods'] = 'GET, PUT, POST, DELETE, HEAD, OPTIONS'
    response['access-control-allow-headers'] = 'Content-Type, Authorization'
    response['Content-Type'] = 'application/json'
    return response