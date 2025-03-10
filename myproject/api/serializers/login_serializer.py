from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    """Serializer để nhận username và password từ request"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
