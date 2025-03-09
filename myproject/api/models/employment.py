from django.db import models
from .group import Group
from .account import Account

class Employment(models.Model):
    position = models.CharField(max_length=255)
    start_date = models.TimeField
    end_date = models.TextField
    qualification = models.CharField(max_length=255)
    year_exp = models.CharField(max_length=2)
    
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="employments")
    account = models.ForeignKey(Account, on_delete= models.CASCADE, related_name="account")
    