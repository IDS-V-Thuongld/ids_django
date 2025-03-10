from rest_framework import viewsets
from api.models import TaskAssignment
from api.serializers.task_assignment_serializer import TaskAssignmentSerializer

class TaskAssignmentViewSet(viewsets.ModelViewSet):
    """
    API CRUD cho Task Assignment:
    - GET: Lấy danh sách task assignments
    - POST: Gán task cho nhân viên
    - PUT/PATCH: Cập nhật tiến độ task
    - DELETE: Xóa task assignment
    """
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

    def perform_destroy(self, instance):
        """Xóa mềm (soft delete) task assignment"""
        instance.is_delete = True
        instance.save()
