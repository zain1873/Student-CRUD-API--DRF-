from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        return Response ({"message": "public can view this data"}) 
    elif request.method == 'POST':
        return Response ({"message": f"data is created by {request.user.username }"})