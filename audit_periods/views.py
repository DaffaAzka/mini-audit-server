from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from audit_periods.services import approve_audit_period
from units import serializer
from .serializer import AuditPeriodSerializer
from .models import AuditPeriod

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list(request):
    audit_periods = AuditPeriod.objects.all()
    serializer = AuditPeriodSerializer(audit_periods, many=True)
    return Response({"message": "Audit periods retrieved successfully", "data": serializer.data}, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = AuditPeriodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Audit period created successfully", "data": serializer.data}, status=201)
    return Response({"message": "Failed to create audit period", "errors": serializer.errors}, status=400)  

@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, pk):    
    try:
        audit_period = AuditPeriod.objects.get(pk=pk)
    except AuditPeriod.DoesNotExist:
        return Response({"message": "Audit period not found"}, status=404)
    
    if request.method == 'GET':
        serializer = AuditPeriodSerializer(audit_period)
        return Response({"message": "Audit period retrieved successfully", "data": serializer.data}, status=200)
    
    elif request.method == 'DELETE':
        audit_period.delete()
        return Response({"message": "Audit period deleted successfully"}, status=204)
    
    elif request.method == 'PUT':
        serializer = AuditPeriodSerializer(audit_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Audit period updated successfully", "data": serializer.data}, status=200)
        return Response({"message": "Failed to update audit period", "errors": serializer.errors}, status=400)
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def approve(request, pk):
    try:
        audit_period = AuditPeriod.objects.get(pk=pk)
        audit_period_after = approve_audit_period(audit_period, request.data.get('comment', ''), request.user)
        serializer = AuditPeriodSerializer(audit_period_after)
        return Response({"message": "Audit period approved successfully", "data": serializer.data}, status=200)
    except AuditPeriod.DoesNotExist:
        return Response({"message": "Audit period not found"}, status=404)
    except ValueError as e:
        return Response({"message": str(e)}, status=400)
    


