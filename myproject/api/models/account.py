from django.db import models

class Account (models.Model):
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True) 
    password = models.TextField
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField
    day_of_birth = models.DateField
    
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
        
    def __str__():
        return super().__str__()
    