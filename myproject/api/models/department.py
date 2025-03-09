from django.db import models
from .company import Company

class Department (models.Model):
    department_name = models.CharField(max_length=255, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="departments")
    
    def __str__(self):
        return super().__str__() 
    