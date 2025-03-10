from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api.models import Account, Employment, Department

class EmploymentSerializer(serializers.ModelSerializer):
    """Serializer để xử lý Employment"""

    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department'
    )  # Nhận department_id thay vì object

    class Meta:
        model = Employment
        fields = ['position', 'start_date', 'end_date', 'qualification', 'year_exp', 'department_id']

class AccountSerializer(serializers.ModelSerializer):
    """Serializer để tạo Account và tự động tạo Employment"""

    employment = EmploymentSerializer(required=True)  # Bắt buộc phải có employment khi tạo account

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'full_name', 'phone', 'address', 'day_of_birth', 'employment']
        extra_kwargs = {
            'password': {'write_only': True},  # Không trả password về response
        }

    def create(self, validated_data):
        """Tạo Account và tự động tạo Employment"""

        employment_data = validated_data.pop('employment')  # Lấy dữ liệu employment
        validated_data['password'] = make_password(validated_data['password'])  # Hash password

        account = Account.objects.create(**validated_data)  # Tạo tài khoản

        # Tạo Employment gắn với Account
        Employment.objects.create(account=account, **employment_data)

        return account
