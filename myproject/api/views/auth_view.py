from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from api.models.account import Account
from api.serializers.login_serializer import LoginSerializer
from api.serializers.account_serializer import AccountSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class LoginView(APIView):
    """API đăng nhập"""
    serializer_class = LoginSerializer  # Swagger cần serializer để hiển thị form
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: openapi.Response("Success", LoginSerializer)}
    )
    def post(self, request):
        """Xác thực đăng nhập bằng cách kiểm tra mật khẩu hash"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = Account.objects.get(username=username)
            except Account.DoesNotExist:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

            # So sánh password đã hash
            if check_password(password, user.password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
