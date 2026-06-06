from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import Group

# Create your models here.
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        
    def create(self, validated_data):
        group = Group.objects.create(
            name=validated_data['name'],
        )
        group.save()
        return group