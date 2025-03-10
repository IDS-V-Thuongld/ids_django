from rest_framework import serializers
from api.models.department import Department
from api.models.company import Company

class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer cho model Department"""

    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company'
    )  # Chỉ nhận company_id thay vì object

    class Meta:
        model = Department
        fields = ['department_name', 'company_id']

    def create(self, validated_data):
        """Tạo department mới"""
        return Department.objects.create(**validated_data)
