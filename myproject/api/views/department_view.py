from rest_framework import viewsets
from api.serializers.department_serializer import DepartmentSerializer
from api.models.department import Department

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer