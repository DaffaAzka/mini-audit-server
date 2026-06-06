
from units.models import Unit
from rest_framework import serializers


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
    def create(self, validated_data):
        unit = Unit.objects.create(
            name=validated_data['name'],
            code=validated_data['code']
        )
        unit.save()
        return unit