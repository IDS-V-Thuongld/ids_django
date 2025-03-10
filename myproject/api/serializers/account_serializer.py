from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api.models.account import Account
class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'full_name', 'phone', 'address', 'day_of_birth']
        extra_kwargs = {
            'password': {'write_only': True},  # Không trả password về response
        }

    def create(self, validated_data):
        """Ghi đè create để hash password trước khi lưu"""
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)