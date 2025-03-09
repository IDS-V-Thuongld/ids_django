from django.db import models
from .department import Department
class Group(models.Model):    
    group_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="groups")
    
    def __str__(self):
        return super().__str__()