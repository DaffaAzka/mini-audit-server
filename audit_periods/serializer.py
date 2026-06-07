from rest_framework import serializers
from .models import AuditPeriod
class AuditPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditPeriod
        fields = ['id', 'unit_id', 'name', 'start_date', 'end_date', 'unit']
        
    def create(self, validated_data):
        audit_period = AuditPeriod.objects.create(
            unit_id=validated_data['unit_id'],
            name=validated_data['name'],
            start_date=validated_data['start_date'],
            end_date=validated_data['end_date']
        )
        return audit_period