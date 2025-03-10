from rest_framework import viewsets
from api.models import Task
from api.serializers.task_serializer import TaskSerializer
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg import openapi
class TaskViewSet(viewsets.ModelViewSet):
    """
    API CRUD cho Task:
    - GET: Lấy danh sách task hoặc task cụ thể
    - POST: Tạo task mới
    - PUT/PATCH: Cập nhật task
    - DELETE: Xóa task (Soft delete)
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        """Lọc danh sách Task theo nhiều điều kiện từ query parameters"""
        queryset = Task.objects.all()
        issue_type = self.request.query_params.get('issue_type', None)
        status = self.request.query_params.get('status', None)
        priority = self.request.query_params.get('priority', None)
        keyword = self.request.query_params.get('keyword', None)

        filters = Q()

        if issue_type:
            filters &= Q(issue_type=issue_type)
        if status:
            filters &= Q(status=status)
        if priority:
            filters &= Q(priority=priority)
        if keyword:
            filters &= Q(title__icontains=keyword) | Q(id__icontains=keyword)

        return queryset.filter(filters)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('issue_type', openapi.IN_QUERY, description="Lọc theo loại task (1 = Task, 2 = Bug)", type=openapi.TYPE_INTEGER),
            openapi.Parameter('status', openapi.IN_QUERY, description="Lọc theo trạng thái (1 = Open, 2 = In Progress, ...)", type=openapi.TYPE_INTEGER),
            openapi.Parameter('priority', openapi.IN_QUERY, description="Lọc theo mức độ ưu tiên (0 = Normal, 1 = Priority)", type=openapi.TYPE_INTEGER),
            openapi.Parameter('keyword', openapi.IN_QUERY, description="Tìm theo tiêu đề hoặc ID task", type=openapi.TYPE_STRING),
        ],
        responses={200: TaskSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_tasks(self, request):
        """Tìm kiếm Task theo Issue Type, Status, Priority, hoặc Keyword"""
        tasks = self.get_queryset()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    def perform_destroy(self, instance):
        """Xóa mềm (soft delete) task thay vì xóa vật lý"""
        instance.is_delete = True
        instance.save()

