from rest_framework import serializers
from .models import AuditTeam

class AuditTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuditTeam
        fields = '__all__'
        
    def create(self, validated_data):
        return super().create(validated_data)