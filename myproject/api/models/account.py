from django.db import models

class Account (models.Model):
    
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True) 
    password = models.TextField
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField
    day_of_birth = models.DateField
    
    def __str__():
        return super().__str__()
    