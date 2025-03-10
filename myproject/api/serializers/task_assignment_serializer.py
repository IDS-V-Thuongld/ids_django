from rest_framework import serializers
from api.models import Task, Employment, TaskAssignment

class TaskAssignmentSerializer(serializers.ModelSerializer):
    """Serializer để gán Task cho nhân viên"""

    task_id = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), source='task'
    )  
    assignee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employment.objects.all(), source='assignee'
    )  

    class Meta:
        model = TaskAssignment
        fields = ['id', 'task_id', 'assignee_id', 'completed', 'completion_date', 'progress']