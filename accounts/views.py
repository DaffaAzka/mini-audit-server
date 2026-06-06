from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import UserSerializer
from rest_framework.permissions import AllowAny 
# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({"messages": "User registered successfully", 'token': token.key}, status=201)
    return Response(serializer.errors, status=400)