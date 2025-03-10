from rest_framework import serializers
from api.models.group import Group

class GroupSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ['group_name', 'description']

    def create(self, validated_data):
        return Group.objects.create(**validated_data)