from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser 
from rest_framework.authentication import TokenAuthentication
from .models import GroupSerializer
from django.contrib.auth.models import Group

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def list(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response({"message": "Groups retrieved successfully", "data": serializer.data}, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def create(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Group created successfully", "data": serializer.data}, status=201)
    return Response({"message": "Failed to create group", "errors": serializer.errors}, status=400)

@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def detail(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response({"message": "Group not found"}, status=404)
    
    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return Response({"message": "Group retrieved successfully", "data": serializer.data}, status=200)
    
    elif request.method == 'DELETE':
        group.delete()
        return Response({"message": "Group deleted successfully"}, status=204)
    
    elif request.method == 'PUT':
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Group updated successfully", "data": serializer.data}, status=200)
        return Response({"message": "Failed to update group", "errors": serializer.errors}, status=400)
