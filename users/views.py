from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser 
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import UserGroupAssignmentSerializer, UserSerializer

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({"message": "retrieved users successfully", "data": serializer.data}, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully", "data": serializer.data}, status=201)
    return Response({"message": "Failed to create user", "errors": serializer.errors}, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=404)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response({"message": "User retrieved successfully", "data": serializer.data}, status=200)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response({"message": "User deleted successfully"}, status=204)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully", "data": serializer.data}, status=200)
        return Response({"message": "Failed to update user", "errors": serializer.errors}, status=400)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def assign_user_to_group(request):
    serializer = UserGroupAssignmentSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": "User assigned to group successfully"}, status=200)
    return Response({"message": "Failed to assign user to group", "errors": serializer.errors}, status=400)
