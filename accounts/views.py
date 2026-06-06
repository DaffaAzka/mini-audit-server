from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny 
from django.contrib.auth import authenticate

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({"message": "User registered successfully", 'token': token.key}, status=201)
    return Response({"message": "Failed to register user", "errors": serializer.errors}, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"message": "Login successful", 'token': token.key}, status=200)
    return Response({"message": "Invalid credentials"}, status=400)