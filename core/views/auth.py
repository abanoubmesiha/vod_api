from urllib import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def login(request):
    content = {'message': 'Hello, World!'}
    return Response(content)

@api_view(['POST'])
def get_token(request):
    response = Response({'token': 'token.key'})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST"
    response["Access-Control-Allow-Headers"] = "*"
    return response
