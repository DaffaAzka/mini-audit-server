from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import serializers

from groups.models import GroupSerializer

# Create your models here.

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True) 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'groups'] 
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UserGroupAssignmentSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    group_id = serializers.IntegerField()
    
    def validate(self, data):
        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        
        try:
            group = Group.objects.get(id=data['group_id'])
        except Group.DoesNotExist:
            raise serializers.ValidationError("Group not found")
        
        data['user'] = user
        data['group'] = group
        return data
    
    def create(self, validated_data):
        user = validated_data['user']
        group = validated_data['group']
        user.groups.add(group)
        return user



