from rest_framework import viewsets, serializers
from api.models import Account
from api.serializers.account_serializer import AccountSerializer, EmploymentSerializer


class AccountView(viewsets.ModelViewSet):
    """
    API CRUD cho tài khoản
    - GET: Lấy danh sách tài khoản hoặc tài khoản cụ thể
    - POST: Tạo tài khoản mới (tạo cả Employment & Department)
    - PUT: Cập nhật tài khoản
    - DELETE: Xóa tài khoản (Soft delete)
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        """Tạo tài khoản và tự động tạo Employment"""
        employment_data = self.request.data.get('employment')  # Lấy dữ liệu employment từ request
        account = serializer.save()  # Lưu tài khoản

        if employment_data:
            employment_serializer = EmploymentSerializer(data=employment_data)
            if employment_serializer.is_valid():
                employment_serializer.save(account=account)  # Tạo Employment gắn với Account
            else:
                account.delete()  # Nếu employment không hợp lệ, rollback lại Account
                raise serializers.ValidationError(employment_serializer.errors)

    def perform_destroy(self, instance):
        """Xóa mềm (soft delete) tài khoản thay vì xóa vật lý"""
        instance.is_delete = True
        instance.save()
