from django.db import models

class Company(models.Model):
    
    company_name = models.CharField(max_length=255)
    address = models.TextField
    website = models.URLField(blank=True, null=True)
    telephone = models.CharField(max_length=10)
    tax_code = models.CharField(max_length=13)
    
    def __str__(self):
        return super().__str__()