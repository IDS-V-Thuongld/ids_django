from rest_framework import viewsets
from api.models.company import Company
from api.serializers.company_serializer import CompanySerializer
class CompanyView (viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer