from rest_framework import viewsets
from api.serializers.group_serializer import GroupSerializer
from api.models.group import Group

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer