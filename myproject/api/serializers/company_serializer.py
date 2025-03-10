from rest_framework import serializers
from api.models.company import Company

class CompanySerializer(serializers.ModelSerializer):
    """Serializer cho model Company"""
    
    class Meta:
        model = Company
        fields = ['company_name', 'tax_code', 'address', 'website', 'telephone']
    
    def create(self, validated_data):
        """Tạo Company mới"""
        return Company.objects.create(**validated_data)
