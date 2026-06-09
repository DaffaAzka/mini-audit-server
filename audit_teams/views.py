from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import AuditTeamSerializer
from .models import AuditTeam

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list(request, pk):
    audit_team = AuditTeam.objects.filter(audit_period_id=audit_period_id)
    serializer = AuditTeamSerializer(audit_team, many=True)
    return Response({"message": "Audit teams retrieved successfully", "data": serializer.data}, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = AuditTeamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Audit team created successfully", "data": serializer.data}, status=201)
    return Response({"message": "Failed to create audit team", "errors": serializer.errors}, status=400)  

@api_view(['DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, pk):    
    try:
        audit_team = AuditTeam.objects.get(pk=pk)
    except AuditTeam.DoesNotExist:
        return Response({"message": "Audit team not found"}, status=404)
    if request.method == 'DELETE':
        audit_team.delete()
        return Response({"message": "Audit team deleted successfully"}, status=204)
    
    elif request.method == 'PUT':
        serializer = AuditTeamSerializer(audit_team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Audit team updated successfully", "data": serializer.data}, status=200)
        return Response({"message": "Failed to update audit team", "errors": serializer.errors}, status=400)


