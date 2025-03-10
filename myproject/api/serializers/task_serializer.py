from rest_framework import serializers
from api.models.task import Task
from api.models.group import Group

class TaskSerializer(serializers.ModelSerializer):
    """Serializer cho model Task"""
    
    assigned_group_id = serializers.PrimaryKeyRelatedField(
        queryset = Group.objects.all(), source='assigned_group', required=False
    )  # Chỉ nhận assigned_group_id thay vì object

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'issue_type', 'priority',
            'create_user', 'start_date', 'due_date', 'estimated_hours', 'assigned_group_id'
        ]