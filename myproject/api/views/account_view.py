from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models.account import Account
from api.serializers.account_serializer import AccountSerializer

class AccountView(viewsets.ModelViewSet):
    """
    API CRUD cho tài khoản
    - GET: Lấy danh sách tài khoản hoặc tài khoản cụ thể
    - POST: Tạo tài khoản mới
    - PUT: Cập nhật tài khoản
    - DELETE: Xóa tài khoản
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
