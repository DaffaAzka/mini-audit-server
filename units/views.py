from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser 
from rest_framework.authentication import TokenAuthentication

from units.serializer import UnitSerializer
from .models import Unit

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def list(request):
    units = Unit.objects.all()
    serializer = UnitSerializer(units, many=True)
    return Response({"message": "Units retrieved successfully", "data": serializer.data}, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def create(request):
    serializer = UnitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Unit created successfully", "data": serializer.data}, status=201)
    return Response({"message": "Failed to create unit", "errors": serializer.errors}, status=400)  

@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def detail(request, pk):    
    try:
        unit = Unit.objects.get(pk=pk)
    except Unit.DoesNotExist:
        return Response({"message": "Unit not found"}, status=404)
    
    if request.method == 'GET':
        serializer = UnitSerializer(unit)
        return Response({"message": "Unit retrieved successfully", "data": serializer.data}, status=200)
    
    elif request.method == 'DELETE':
        unit.delete()
        return Response({"message": "Unit deleted successfully"}, status=204)
    
    elif request.method == 'PUT':
        serializer = UnitSerializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Unit updated successfully", "data": serializer.data}, status=200)
        return Response({"message": "Failed to update unit", "errors": serializer.errors}, status=400)
