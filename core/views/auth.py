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
    return Response(
        {'token': 'token.key'},
        headers={
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods" : "POST",
            "Access-Control-Allow-Headers" : "*",
        }
    )
