from django.db import models

class Company(models.Model):
    
    company_name = models.CharField(max_length=255)
    address = models.TextField
    website = models.URLField(blank=True, null=True)
    telephone = models.CharField(max_length=10)
    tax_code = models.CharField(max_length=13)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    is_delete = models.BooleanField(default=False)  # Cờ đánh dấu xóa (0 = active, 1 = deleted)

    def soft_delete(self):
        """Đánh dấu bản ghi là đã xóa thay vì xóa vật lý"""
        self.is_delete = True
        self.save()

    def restore(self):
        """Khôi phục bản ghi đã bị đánh dấu xóa"""
        self.is_delete = False
        self.save()
        
    def __str__(self):
        return super().__str__()